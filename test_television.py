import pytest
from television import Television


def test_init():
    """Test the default television settings."""
    tv = Television()

    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power():
    """Test turning the television on and off."""
    tv = Television()

    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute():
    """Test muting and unmuting the television."""
    tv = Television()

    tv.power()
    tv.volume_up()
    tv.mute()

    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.mute()
    tv.power()
    tv.mute()
    tv.power()

    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_up():
    """Test increasing the television channel."""
    tv = Television()

    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_up()

    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    tv.channel_up()
    tv.channel_up()
    tv.channel_up()

    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down():
    """Test decreasing the television channel."""
    tv = Television()

    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_down()

    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    tv.channel_down()

    assert str(tv) == "Power = True, Channel = 2, Volume = 0"


def test_volume_up():
    """Test increasing the television volume."""
    tv = Television()

    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.volume_up()

    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down():
    """Test decreasing the television volume."""
    tv = Television()

    tv.power()
    tv.volume_down()

    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_up()
    tv.volume_up()
    tv.volume_down()

    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_volume_up_when_muted():
    """Test that increasing volume automatically unmutes the television."""
    tv = Television()

    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_up()

    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down_when_muted():
    """Test that decreasing volume automatically unmutes the television."""
    tv = Television()

    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    tv.volume_down()

    assert str(tv) == "Power = True, Channel = 0, Volume = 1"