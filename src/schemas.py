from datetime import date

from pydantic import BaseModel, validator, ValidationError


class QuestionRequestParamsSchema(BaseModel):
    questions_num: int = 1

    @validator("questions_num")
    def questions_num_ge_than_1_and_lt_100(cls, v):
        if not 1 <= v <= 100:
            raise ValueError('questions_num must be greather or equal 1 and equal or less than 100!')
        return v

class QuestionSchema(BaseModel):
    id: int
    answer: str
    text: str
    creation_date: date
