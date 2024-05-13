import logging
from astropy.table import Table, Column

logger = logging.getLogger(__name__)


class LightCurve:
    def __init__(
        self,
        time=None,
        y=None,
        time_err=None,
        y_err=None,
        time_unit=None,
        y_unit=None,
        **kwargs,
    ) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

        try:
            self.time = Column(time, name="Time", unit=time_unit)
            self.y = Column(y, name="Y", unit=y_unit)
            self.time_err = Column(time_err, name="Time errors", unit=time_unit)
            self.y_err = Column(y_err, name="Y errors", unit=y_unit)
            assert (
                len(self.time) == len(self.y) == len(self.time_err) == len(self.y_err)
            )
        except AssertionError:
            logger.error(
                "Column length mismatch. Provided column length of" +
                f"Time: {len(self.time)}, y: {len(self.y)}, " +
                f"time_err: {len(self.time_err)}, and y_err: {len(self.yerr)} " +
                "does not match"
            )

    def read(self, filename: str, format="ascii", **kwargs):
        try:
            self.data = Table.read(filename, format=format, **kwargs)
        except FileNotFoundError:
            raise FileNotFoundError

    def __repr__(self):
        return repr(self.data)
