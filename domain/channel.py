from typing import Iterable
from pydantic import BaseModel, validator, ValidationError
from decimal import Decimal

class Channel(BaseModel):
    name: str
    description: str | None = None
    count_of_subscribers: int
    language: str | None = None
    rating: Decimal | None = None  # rating from 1 to 5

    def put_channel_rating(self, rating: int):
        if rating < 1 or rating > 5:
            raise ValidationError('Rate must be range from 1 to 5')
        self.rating = rating if self.rating is None else round((self.rating + rating) / 2, 2)

    @validator('name')
    def validate_name(cls, name: str) -> str:
        cls._validate_max_length('name', name, 128)
        return name

    @validator('description')
    def validate_description(cls, description: str | None) -> str | None:
        if description is not None:
            cls._validate_max_length('description', description, 255)
        return description

    @validator('count_of_subscribers')
    def validate_count_of_subscribers(cls, count: int | None) -> int:
        if count <= 0:
            raise ValidationError('Count of subscribers must be great than 0')
        return count

    @validator('language')
    def validate_language(cls, lang: str) -> str:
        if lang is not None and len(lang) > 2:
            raise ValidationError('Language must be in ISO2 format')
        return lang.upper()
    
    @validator('rating')
    def validate_rating(cls, rating: Decimal | None) -> Decimal:
        if rating is not None and (rating < 1 or rating > 5):
            raise ValidationError('Rating must be range from 1 to 5')
        return round(rating, 2)

    @staticmethod
    def _validate_max_length(field_name: str, iterable_obj: Iterable, max_len: int):
        if len(iterable_obj) > max_len:
            raise ValidationError(f'{field_name.capitalize()} must be great than {max_len}')
    
    