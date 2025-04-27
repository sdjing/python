import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"

def test_power_on_off():
    tv = Television()
    tv.power()
    assert str(tv).startswith("Power = On")
    tv.power()
    assert str(tv).startswith("Power = Off")

def test_mute_unmute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert "Volume" in str(tv)
    tv.mute()
    assert "Volume" in str(tv)

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert "Channel = 1" in str(tv)
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert "Channel = 0" in str(tv)  

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert "Channel = 3" in str(tv) 
    tv.channel_down()
    assert "Channel = 2" in str(tv)

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert "Volume = 1" in str(tv)
    tv.volume_up()
    tv.volume_up()
    assert "Volume = 2" in str(tv)  

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert "Volume = 1" in str(tv)
    tv.volume_down()
    tv.volume_down()
    assert "Volume = 0" in str(tv)  
