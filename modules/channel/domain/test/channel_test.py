from collections import deque
import pytest
from datetime import datetime, timedelta
from modules.channel.domain.entities import Channel



@pytest.fixture
def valid_channel():
    return Channel(**{
        'name': 'Some name',
        'description': 'Some description',
        'count_of_subscribers': 1523,
        'added_at': datetime.now(),
        'language': 'ua',
        'rates': [1, 2, 3, 4, 5, 5, 3, 4, 5, 3],
    })


def test_put_rate(valid_channel: Channel):
    valid_channel.put_rate(3)
    assert valid_channel.rates == deque([2, 3, 4, 5, 5, 3, 4, 5, 3, 3])


@pytest.mark.parametrize('rate', (0, 6, 1.5))
def test_raise_put_channel_rating(valid_channel: Channel, rate):
    with pytest.raises(ValueError):
        valid_channel.put_rate(rate)


def test_compute_rating(valid_channel: Channel):
    assert valid_channel.compute_rating() == 3.5


def test_compute_rating_with_empty_rates(valid_channel: Channel):
    valid_channel.rates = []
    with pytest.raises(ValueError):
        valid_channel.compute_rating()


def test_validation_long_name(valid_channel: Channel):
    with pytest.raises(TypeError):
        channel_data = valid_channel.dict()
        channel_data['name'] = 'a' * 129
        Channel(**valid_channel)


@pytest.mark.parametrize('lang', ('FG', 'Adsada'))
def test_raise_validation_iso2_lang(valid_channel: Channel, lang: str):
    with pytest.raises(ValueError):
        valid_channel.validate_language(lang)


@pytest.mark.parametrize('lang', ('Ua', 'uA'))
def test_validation_iso2_lang(valid_channel: Channel, lang: str):
    assert valid_channel.validate_language(lang) == lang.upper()


def test_raise_validate_rates(valid_channel: Channel):
    with pytest.raises(ValueError):
        valid_channel.validate_rates(range(11))


def test_validate_rates(valid_channel: Channel):
    rates = [1, 2, 3, 4, 3]
    validated_rates = valid_channel.validate_rates(rates)
    assert isinstance(validated_rates, deque)
    assert validated_rates == deque(rates)
    assert validated_rates.maxlen == 10


def test_raise_validation_added_at(valid_channel: Channel):
    future_datetime = datetime.now() + timedelta(days=1)
    with pytest.raises(ValueError):
        valid_channel.validate_added_at(future_datetime)


def test_validation_added_at(valid_channel: Channel):
    now_datetime = datetime.now()
    assert valid_channel.validate_added_at(now_datetime) == now_datetime
