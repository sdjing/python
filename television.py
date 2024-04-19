class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''Initializes default values'''
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        '''Turns the power on or off'''
        self.__status = not self.__status

    def mute(self):
        '''Mutes the volume'''
        self.__muted = not self.__muted

    def channel_up(self):
        '''Increases the TV channel'''
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        '''Decreases the TV channel'''
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        '''Increases the TV volume'''
        if self.__status:
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
                self.__muted = False

    def volume_down(self):
        '''Decreases the TV volume'''
        if self.__status:
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
                self.__muted = False

    def __str__(self):
        '''Returns a string with the values of the objects'''
        power_status = "On" if self.__status else "Off"
        return f"Power = [{power_status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"
    