class Television:
    """A class representing a Television with basic functionality."""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initializes television"""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """Turns television on and off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """If television is on, mutes it."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increases the channel by one."""
        if self.__status:
            self.__channel = (self.__channel + 1) if self.__channel < self.MAX_CHANNEL else self.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decreases the channel by one."""
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > self.MIN_CHANNEL else self.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume by one or unmute if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by one or unmute if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the television's status as a formatted string."""
        power_status = "On" if self.__status else "Off"
        return f"Power = {power_status}, Channel = {self.__channel}, Volume = {self.__volume}"
