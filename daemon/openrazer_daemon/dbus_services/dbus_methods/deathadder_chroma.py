from openrazer_daemon.dbus_services import endpoint


@endpoint('razer.device.lighting.backlight', 'getBacklightActive', out_sig='b')
def get_backlight_active(self):
    """
    Get if the backlight is lit up

    :return: Active
    :rtype: bool
    """
    self.logger.debug("DBus call get_backlight_active")

    return self._read_10('backlight_led_state')


@endpoint('razer.device.lighting.backlight', 'setBacklightActive', in_sig='b')
def set_backlight_active(self, active):
    """
    Get if the backlight is lit up

    :param active: Is active
    :type active: bool
    """
    self.logger.debug("DBus call set_backlight_active")

    self._write_10('backlight_led_state', active)


@endpoint('razer.device.lighting.logo', 'getLogoActive', out_sig='b')
def get_logo_active(self):
    """
    Get if the logo is light up

    :return: Active
    :rtype: bool
    """
    self.logger.debug("DBus call get_logo_active")

    return self._read_10('logo_led_state')


@endpoint('razer.device.lighting.logo', 'setLogoActive', in_sig='b')
def set_logo_active(self, active):
    """
    Get if the logo is light up

    :param active: Is active
    :type active: bool
    """
    self.logger.debug("DBus call set_logo_active")

    self._write_10('logo_led_state', active)


@endpoint('razer.device.lighting.logo', 'getLogoEffect', out_sig='y')
def get_logo_effect(self):
    """
    Get logo effect

    :return: Active
    :rtype: bool
    """
    self.logger.debug("DBus call get_logo_effect")

    return self._read_int('logo_led_effect')


@endpoint('razer.device.lighting.logo', 'getLogoBrightness', out_sig='d')
def get_logo_brightness(self):
    """
    Get the device's brightness

    :return: Brightness
    :rtype: float
    """
    self.logger.debug("DBus call get_logo_brightness")

    return self._read_percent('logo_led_brightness', maxval=255)

@endpoint('razer.device.lighting.logo', 'setLogoBrightness', in_sig='d')
def set_logo_brightness(self, brightness):
    """
    Set the device's brightness

    :param brightness: Brightness
    :type brightness: int
    """
    self.logger.debug("DBus call set_logo_brightness")

    self.cached_values['brightness'] = brightness
    brightness = self._write_percent('logo_led_brightness', brightness, maxval=255)

    # Notify others
    self.send_effect_event('setBrightness', brightness)


@endpoint('razer.device.lighting.logo', 'setLogoStatic', in_sig='yyy')
def set_logo_static(self, red, green, blue):
    """
    Set the device to static colour

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_static_effect")

    # Notify others
    self.send_effect_event('setStatic', red, green, blue)

    self._write_bytes('logo_led_rgb', [red, green, blue])
    self._write_int('logo_led_effect', 0)

@endpoint('razer.device.lighting.logo', 'setLogoBlinking', in_sig='yyy')
def set_logo_blinking(self, red, green, blue):
    """
    Set the device to pulsate

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_logo_blinking")

    # Notify others
    self.send_effect_event('setLogoBlinking', red, green, blue)

    self._write_bytes('logo_led_rgb', [red, green, blue])
    self._write_int('logo_led_effect', 1)


@endpoint('razer.device.lighting.logo', 'setLogoPulsate', in_sig='yyy')
def set_logo_pulsate(self, red, green, blue):
    """
    Set the device to pulsate

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_logo_pulsing")

    # Notify others
    self.send_effect_event('setPulsate', red, green, blue)

    self._write_bytes('logo_led_rgb', [red, green, blue])
    self._write_int('logo_led_effect', 2)


@endpoint('razer.device.lighting.logo', 'setLogoSpectrum')
def set_logo_spectrum(self):
    """
    Set the device to pulsate

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_logo_spectrum")

    # Notify others
    self.send_effect_event('setSpectrum')

    self._write_int('logo_led_effect', 4)


@endpoint('razer.device.lighting.scroll', 'getScrollActive', out_sig='b')
def get_scroll_active(self):
    """
    Get if the scroll is light up

    :return: Active
    :rtype: bool
    """
    self.logger.debug("DBus call get_scroll_active")

    return self._read_10('scroll_led_state')

@endpoint('razer.device.lighting.scroll', 'setScrollActive', in_sig='b')
def set_scroll_active(self, active):
    """
    Get if the scroll is light up

    :param active: Is active
    :type active: bool
    """
    self.logger.debug("DBus call set_scroll_active")

    self._write_10('scroll_led_state', active)


@endpoint('razer.device.lighting.scroll', 'getScrollEffect', out_sig='y')
def get_scroll_effect(self):
    """
    Get scroll effect

    :return: Active
    :rtype: bool
    """
    self.logger.debug("DBus call get_scroll_effect")

    return self._read_int('scroll_led_effect')


@endpoint('razer.device.lighting.scroll', 'getScrollBrightness', out_sig='d')
def get_scroll_brightness(self):
    """
    Get the device's brightness

    :return: Brightness
    :rtype: float
    """
    self.logger.debug("DBus call get_scroll_brightness")

    return self._read_percent('scroll_led_brightness', maxval=255)


@endpoint('razer.device.lighting.scroll', 'setScrollBrightness', in_sig='d')
def set_scroll_brightness(self, brightness):
    """
    Set the device's brightness

    :param brightness: Brightness
    :type brightness: int
    """
    self.logger.debug("DBus call set_scroll_brightness")

    self.cached_values['brightness'] = brightness
    brightness = self._write_percent('scroll_led_brightness', brightness, maxval=255)

    # Notify others
    self.send_effect_event('setBrightness', brightness)


@endpoint('razer.device.lighting.scroll', 'setScrollStatic', in_sig='yyy')
def set_scroll_static(self, red, green, blue):
    """
    Set the device to static colour

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_scroll_static")

    # Notify others
    self.send_effect_event('setStatic', red, green, blue)

    self._write_bytes('scroll_led_rgb', [red, green, blue])
    self._write_int('scroll_led_effect', 0)


@endpoint('razer.device.lighting.scroll', 'setScrollBlinking', in_sig='yyy')
def set_scroll_blinking(self, red, green, blue):
    """
    Set the device to pulsate

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_scroll_pulsate")

    # Notify others
    self.send_effect_event('setPulsate', red, green, blue)

    self._write_bytes('scroll_led_rgb', [red, green, blue])
    self._write_int('scroll_led_effect', 1)


@endpoint('razer.device.lighting.scroll', 'setScrollPulsate', in_sig='yyy')
def set_scroll_pulsate(self, red, green, blue):
    """
    Set the device to pulsate

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_scroll_breathing")

    # Notify others
    self.send_effect_event('setPulsate', red, green, blue)

    self._write_bytes('scroll_led_rgb', [red, green, blue])
    self._write_int('scroll_led_effect', 2)


@endpoint('razer.device.lighting.scroll', 'setScrollSpectrum')
def set_scroll_spectrum(self):
    """
    Set the device to pulsate

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_scroll_spectrum")

    # Notify others
    self.send_effect_event('setSpectrum')

    self._write_int('scroll_led_effect', 4)

