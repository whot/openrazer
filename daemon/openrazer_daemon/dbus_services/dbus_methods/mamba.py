"""
BlackWidow Chroma Effects
"""
import math
import struct
from openrazer_daemon.dbus_services import endpoint


@endpoint('razer.device.power', 'getBattery', out_sig='d')
def get_battery(self):
    """
    Get mouse's battery level
    """
    self.logger.debug("DBus call get_battery")

    # FIXME
    driver_path = self.get_driver_path('charge_level')

    with open(driver_path, 'r') as driver_file:
        battery_255 = float(driver_file.read().strip())
        if battery_255 < 0:
            return -1.0

        battery_100 = (battery_255 / 255) * 100
        return battery_100


@endpoint('razer.device.power', 'isCharging', out_sig='b')
def is_charging(self):
    """
    Get charging status
    """
    self.logger.debug("DBus call is_charging")

    return bool(self._read_int('charge_status'))


@endpoint('razer.device.power', 'setIdleTime', in_sig='q')
def set_idle_time(self, idle_time):
    """
    Set the idle time of the mouse in seconds

    :param idle_time: Idle time in seconds (unsigned short)
    :type idle_time: int
    """
    self.logger.debug("DBus call set_idle_time")

    return self._write_string('device_idle_time', idle_time)


@endpoint('razer.device.power', 'setLowBatteryThreshold', in_sig='y')
def set_low_battery_threshold(self, threshold):
    """
    Set the low battery threshold as a percentage

    :param threshold: Battery threshold as a percentage
    :type threshold: int
    """
    self.logger.debug("DBus call set_low_battery_threshold")

    # FIXME
    driver_path = self.get_driver_path('charge_low_threshold')

    threshold = math.floor((threshold/100) * 255)

    with open(driver_path, 'w') as driver_file:
        driver_file.write(str(threshold))


@endpoint('razer.device.lighting.power', 'setChargeEffect', in_sig='y')
def set_charge_effect(self, charge_effect):
    """
    Set the charging effect.

    If 0x00 then it will use the current mouse's effect
    If 0x01 it will use the charge colour

    :param charge_effect: Charge effect
    :type charge_effect: int
    :return:
    """
    self.logger.debug("DBus call set_charge_effect")

    self._write_bytes('charge_effect', [charge_effect])


@endpoint('razer.device.lighting.power', 'setChargeColour', in_sig='yyy')
def set_charge_colour(self, red, green, blue):
    """
    Set the charge colour

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_charge_colour")

    self._write_bytes('charge_colour', [red, green, blue])


@endpoint('razer.device.dpi', 'setDPI', in_sig='qq')
def set_dpi_xy(self, dpi_x, dpi_y):
    """
    Set the DPI on the mouse, Takes in 4 bytes big-endian

    :param dpi_x: X DPI
    :type dpi_x: int
    :param dpi_y: Y DPI
    :type dpi_x: int
    """
    self.logger.debug("DBus call set_dpi_both")

    dpi_bytes = struct.pack('>HH', dpi_x, dpi_y)

    self._write_bytes('dpi', dpi_bytes)


@endpoint('razer.device.dpi', 'getDPI', out_sig='ai')
def get_dpi_xy(self):
    """
    get the DPI on the mouse

    :return: List of X, Y DPI
    :rtype: list of int
    """
    self.logger.debug("DBus call get_dpi_both")

    dpi_x, dpi_y = [int(dpi) for dpi in self._read_string('dpi')]

    return [dpi_x, dpi_y]


@endpoint('razer.device.dpi', 'maxDPI', out_sig='i')
def max_dpi(self):
    self.logger.debug("DBus call get_dpi_both")

    if hasattr(self, 'DPI_MAX'):
        return self.DPI_MAX

    else:
        return 500



@endpoint('razer.device.misc', 'setPollRate', in_sig='q')
def set_poll_rate(self, rate):
    """
    Set the DPI on the mouse, Takes in 4 bytes big-endian

    :param rate: Poll rate
    :type rate: int
    """
    self.logger.debug("DBus call set_poll_rate")

    if rate in (1000, 500, 125):
        self._write_int('poll_rate', rate)
    else:
        self.logger.error("Poll rate %d is invalid", rate)


@endpoint('razer.device.misc', 'getPollRate', out_sig='i')
def get_poll_rate(self):
    """
    Get the polling rate from the device

    :return: Poll rate
    :rtype: int
    """
    self.logger.debug("DBus call get_poll_rate")

    return self._read_int('poll_rate')


