"""
Module for mug methods
"""
from openrazer_daemon.dbus_services import endpoint

@endpoint('razer.device.misc.mug', 'isMugPresent', out_sig='b')
def is_mug_present(self):
    """
    Get if the mug is present

    :return: True if theres a mug
    :rtype: bool
    """
    self.logger.debug("DBus call is_mug_present")

    return self._read_10('is_mug_present')
