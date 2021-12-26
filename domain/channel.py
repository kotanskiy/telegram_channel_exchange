from typing import Iterable, List, Optional
from _pytest.python_api import raises
from pydantic import BaseModel, validator
from pycountry import countries


class Channel(BaseModel):
    name: str
    description: Optional[str] = None
    count_of_subscribers: int
    language: Optional[str] = None
    rates: List[int]


    def put_rate(self, rate: int):
        if not self._is_valid_rate(rate):
            raise ValueError('Rate must be range from 1 to 5 and integer')
        self.rates.append(rate)


    def compute_rating(self) -> float:
        if not self.rates:
            raise ValueError('Can\'t compute rating without rates')
        return round(sum(self.rates) / len(self.rates), 2)
    

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
            raise ValueError('Count of subscribers must be great than 0')
        return count


    @validator('language')
    def validate_language(cls, lang: str) -> str:
        if lang is None:
            return lang
        exc = ValueError('Language must be in ISO2 format')
        if len(lang) > 2:
            raise exc
        try:
            countries.lookup(lang)
        except LookupError:
            raise exc
        return lang.upper()
    

    @validator('rates')
    def validate_rates(cls, rates: List[int]) -> List[int]:
        '''List of rates from 1 to 5'''
        if not all([cls._is_valid_rate(r) for r in rates]):
            raise ValueError('Rate in rates must be an integer and 1 < rate < 5')
        return rates
    

    @classmethod
    def _is_valid_rate(cls, rate: int):
        return rate >= 1 and rate <= 5 and isinstance(rate, int)


    @staticmethod
    def _validate_max_length(field_name: str, iterable_obj: Iterable, max_len: int):
        if len(iterable_obj) > max_len:
            raise ValueError(f'{field_name.capitalize()} must be less than {max_len}')


__all__ = (
    'Channel',
)
