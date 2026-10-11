from pydantic import BaseModel, Field, field_validator


class PredictRequest(BaseModel):
    text: str = Field(min_length=1)

    @field_validator("text")
    @classmethod
    def text_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Text must not be empty")
        return value


class PredictResponse(BaseModel):
    prediction: str
