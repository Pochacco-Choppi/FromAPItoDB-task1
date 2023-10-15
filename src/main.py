import requests
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import PendingRollbackError, IntegrityError
from datetime import datetime, date

from src.database import engine
from src.models import Question
from src.schemas import QuestionRequestParamsSchema, QuestionSchema



def post_questions_to_db(qestion_count: int=1):
    response = requests.get("https://jservice.io/api/random", params={"count": qestion_count})
    fail_to_insert_count = 0

    for question_data in response.json():
        question_json = QuestionSchema(
            **{
                "id": question_data["id"],
                "answer": question_data["answer"],
                "text": question_data["question"],
                "creation_date": datetime.strptime(question_data["created_at"][:10], "%Y-%m-%d").date(),
                }
            )

        question = Question(**question_json.model_dump())
        with Session(engine) as session:
            try:
                session.add(question)
                session.commit()
            except (PendingRollbackError, IntegrityError):
                fail_to_insert_count += 1
                continue

    if fail_to_insert_count:
        post_questions_to_db(fail_to_insert_count)

    return question_json



def create_app() -> FastAPI:
    app: FastAPI = FastAPI()

    @app.get("/question")
    def list_question() -> JSONResponse:
        with Session(engine) as session:
            questions = session.query(Question).all()

        return jsonable_encoder(questions)

    @app.post("/question")
    def post_question(qr: QuestionRequestParamsSchema) -> JSONResponse:
        questions_count = qr.questions_num

        return jsonable_encoder(post_questions_to_db(questions_count))

    return app

app: FastAPI = create_app()

