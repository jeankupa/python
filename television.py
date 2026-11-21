class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize the television with its default values."""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Turn the television on or off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the television when it is on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel when the television is on."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Decrease the channel when the television is on."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increase volume and unmute the television if necessary."""
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease volume and unmute the television if necessary."""
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the current television power, channel, and volume."""
        if self.__muted:
            volume = Television.MIN_VOLUME
        else:
            volume = self.__volume

        return (f"Power = {self.__status}, "
                f"Channel = {self.__channel}, "
                f"Volume = {volume}")