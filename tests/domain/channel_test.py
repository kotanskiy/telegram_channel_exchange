import pytest
from domain.channel import Channel



@pytest.fixture
def valid_channel():
    return Channel(**{
        'name': 'Some name',
        'description': 'Some description',
        'count_of_subscribers': 1523,
        'language': 'ua',
        'rates': [1, 2],
    })


def test_put_rate(valid_channel: Channel):
    valid_channel.put_rate(3)
    assert valid_channel.rates == [1, 2, 3]


@pytest.mark.parametrize('rate', (0, 6, 1.5))
def test_raise_put_channel_rating(valid_channel: Channel, rate):
    with pytest.raises(ValueError):
        valid_channel.put_rate(rate)


def test_compute_rating(valid_channel: Channel):
    assert valid_channel.compute_rating() == 1.5


def test_compute_rating_with_empty_rates(valid_channel: Channel):
    valid_channel.rates = []
    with pytest.raises(ValueError):
        valid_channel.compute_rating()


def test_validation_long_name(valid_channel: Channel):
    with pytest.raises(ValueError):
        valid_channel.validate_name('a' * 129)


def test_validation_long_description(valid_channel: Channel):
    with pytest.raises(ValueError):
        valid_channel.validate_description('a' * 256)


@pytest.mark.parametrize('count', (0, -1, -200))
def test_validation_negative_count_of_subscribers(valid_channel: Channel, count: int):
    with pytest.raises(ValueError):
        valid_channel.validate_count_of_subscribers(count)



@pytest.mark.parametrize('lang', ('FG', 'Adsada'))
def test_raise_validation_iso2_lang(valid_channel: Channel, lang: str):
    with pytest.raises(ValueError):
        valid_channel.validate_language(lang)


@pytest.mark.parametrize('lang', ('Ua', 'uA'))
def test_validation_iso2_lang(valid_channel: Channel, lang: str):
    assert valid_channel.validate_language(lang) == lang.upper()


@pytest.mark.parametrize('rates', ([1, 2, 3 ,7, 6, 0], [1, 3, 3.5]))
def test_raise_validate_rates(valid_channel: Channel, rates: list):
    with pytest.raises(ValueError):
        valid_channel.validate_rates(rates)
