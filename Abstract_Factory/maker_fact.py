from linuxfact import LinuxMaker as Linux
from windowsfact import WindowsMaker as Windows


class MakerFactory:
    """Factory for creating maker instances."""
    makers = {
        'Linux': Linux,
        'Windows': Windows,
    }

    @staticmethod
    def create_maker(os_type, catalogue):
        if os_type not in MakerFactory.makers:
            raise ValueError(f"Unsupported OS type: {os_type}")
        maker_class = MakerFactory.makers[os_type]
        return maker_class(catalogue)
