"""
BlackWidow Ultimate 2013 effects
"""
from openrazer_daemon.dbus_services import endpoint

@endpoint('razer.device.lighting.bw2013', 'getEffect', out_sig='y')
def bw_get_effect(self):
    """
    Get current effect

    :return: Brightness
    :rtype: int
    """
    self.logger.debug("DBus call bw_get_effect")

    return self._read_int('matrix_effect_pulsate')


@endpoint('razer.device.lighting.bw2013', 'setPulsate')
def bw_set_pulsate(self):
    """
    Set pulsate mode
    """
    self.logger.debug("DBus call bw_set_pulsate")

    driver_path = self.get_driver_path('matrix_effect_pulsate')

    self._write_10('matrix_effect_pulsate', 1)

    # Notify others
    self.send_effect_event('setPulsate')


@endpoint('razer.device.lighting.bw2013', 'setStatic')
def bw_set_static(self):
    """
    Set static mode
    """
    self.logger.debug("DBus call bw_set_static")

    self._write_10('matrix_effect_static', 1)

    # Notify others
    self.send_effect_event('setStatic')



