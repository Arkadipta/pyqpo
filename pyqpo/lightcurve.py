import logging
from astropy.table import Table

logger = logging.getLogger(__name__)

class LightCurve:
    def __init__(self, data = None, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

        try:
            self.data = Table(data, **kwargs)
        except AssertionError:
            logger.error("Could not identify columns")

    def read(self, filename: str, format="ascii", **kwargs):
        try:
            self.data = Table.read(filename, format=format, **kwargs)
        except:
            raise FileNotFoundError

    def __repr__(self):
        return repr(self.data)