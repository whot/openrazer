from openrazer_daemon.dbus_services import endpoint


@endpoint('razer.device.lighting.logo', 'getActive', out_sig='b')
def blade_get_logo_active(self):
    """
    Get if the logo is light up

    :return: Active
    :rtype: bool
    """
    self.logger.debug("DBus call get_logo_active")

    # inverted, see https://github.com/openrazer/openrazer/issues/389
    return 0 if self._read_10('logo_led_state') else 1


@endpoint('razer.device.lighting.logo', 'setActive', in_sig='b')
def blade_set_logo_active(self, active):
    """
    Get if the logo is light up

    :param active: Is active
    :type active: bool
    """
    self.logger.debug("DBus call set_logo_active")

    # inverted, see https://github.com/openrazer/openrazer/issues/389
    self._write_10('logo_led_state', !active)
