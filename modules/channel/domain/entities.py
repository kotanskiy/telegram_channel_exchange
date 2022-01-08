from typing import Any, Deque, Iterable, Optional
from uuid import uuid4
from collections import deque
from functools import partial

from datetime import datetime
from pydantic import validator, Field, constr, conint
from pycountry import countries
from pydantic.types import UUID4

from modules.shared_types.entity import Entity


COUNT_RATES = 10


class Channel(Entity):
    added_at: datetime
    name: constr(min_length=3, max_length=128)
    description: constr(max_length=255) = None
    count_of_subscribers: conint(ge=1)
    language: constr(min_length=2, max_length=2) = None
    rates: Deque[conint(ge=1, le=5)] = Field(default_factory=partial(deque, ([], COUNT_RATES)))


    def put_rate(self, rate: int):
        self._validate_rate(rate)
        self.rates.append(rate)


    @property
    def rate(self) -> Optional[float]:
        if not self.rates:
            return None
        return round(sum(self.rates) / len(self.rates), 2)


    @validator('added_at')
    def validate_added_at(cls, added_at: datetime) -> datetime:
        now = datetime.now()
        if now < added_at:
            raise ValueError('Added at datetime can\'t be in future')
        return added_at


    @validator('language')
    def validate_language(cls, lang: str) -> str:
        try:
            countries.lookup(lang)
        except LookupError:
            raise ValueError('Language must be in ISO2 format')
        return lang.upper()
    

    @validator('rates')
    def validate_rates(cls, rates: Iterable):
        if len(rates) > COUNT_RATES:
            raise ValueError('Rates length must be less than equal 10')
        return deque(rates, COUNT_RATES)


    def _validate_rate(self, rate: Any):
        if not isinstance(rate, int) or rate > 5 or rate < 1:
            raise ValueError('Rate must be integer from 1 to 5')


__all__ = (
    'Channel',
    'COUNT_RATES',
)
