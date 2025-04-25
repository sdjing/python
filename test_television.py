from television import Television

def test_init():
    tv = Television()
    assert tv._Television__status == False
    assert tv._Television__muted == False
    assert tv._Television__volume == tv.MIN_VOLUME
    assert tv._Television__channel == tv.MIN_CHANNEL

def test_power():
    tv = Television()
    tv.power()
    assert tv._Television__status == True
    tv.power()
    assert tv._Television__status == False

def test_mute():
    tv = Television()
    tv.mute()
    assert tv._Television__muted == True
    tv.mute()
    assert tv._Television__muted == False

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv._Television__channel == tv.MIN_CHANNEL + 1
    tv.channel_up()
    assert tv._Television__channel == tv.MIN_CHANNEL + 2

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv._Television__channel == tv.MIN_CHANNEL - 1
    tv.channel_down()
    assert tv._Television__channel == tv.MIN_CHANNEL - 2
    
def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv._Television__volume == tv.MIN_VOLUME + 1
    tv.volume_up()
    assert tv._Television__volume == tv.MIN_VOLUME + 2

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_down()
    assert tv._Television__volume == tv.MIN_VOLUME - 1
    tv.volume_down()
    assert tv._Television__volume == tv.MIN_VOLUME - 2
