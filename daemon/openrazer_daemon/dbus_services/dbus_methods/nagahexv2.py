from openrazer_daemon.dbus_services import endpoint

@endpoint('razer.device.lighting.logo', 'setStatic', in_sig='yyy')
def set_logo_static_naga_hex_v2(self, red, green, blue):
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

    self._write_bytes('logo_matrix_effect_static', [red, green, blue])


@endpoint('razer.device.lighting.logo', 'setSpectrum')
def set_logo_spectrum_naga_hex_v2(self):
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

    self._write_10('logo_matrix_effect_spectrum', 1)


@endpoint('razer.device.lighting.logo', 'setNone')
def set_logo_none_naga_hex_v2(self):
    """
    Set the device to spectrum mode
    """
    self.logger.debug("DBus call set_none_effect")

    # Notify others
    self.send_effect_event('setNone')

    self._write_10('logo_matrix_effect_none', 1)


@endpoint('razer.device.lighting.logo', 'setReactive', in_sig='yyyy')
def set_logo_reactive_naga_hex_v2(self, red, green, blue, speed):
    """
    Set the device to reactive effect

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int

    :param speed: Speed
    :type speed: int
    """
    self.logger.debug("DBus call set_reactive_effect")

    # Notify others
    self.send_effect_event('setReactive', red, green, blue, speed)

    if speed not in (1, 2, 3, 4):
        speed = 4

    self._write_bytes('logo_matrix_effect_reactive', [red, green, blue, speed])


@endpoint('razer.device.lighting.logo', 'setBreathRandom')
def set_logo_breath_random_naga_hex_v2(self):
    """
    Set the device to random colour breathing effect
    """
    self.logger.debug("DBus call set_breath_random_effect")

    # Notify others
    self.send_effect_event('setBreathRandom')

    payload = b'1'

    self._write_bytes('logo_matrix_effect_breath', [payload])


@endpoint('razer.device.lighting.logo', 'setBreathSingle', in_sig='yyy')
def set_logo_breath_single_naga_hex_v2(self, red, green, blue):
    """
    Set the device to single colour breathing effect

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_breath_single_effect")

    # Notify others
    self.send_effect_event('setBreathSingle', red, green, blue)

    self._write_bytes('logo_matrix_effect_breath', [red, green, blue])


@endpoint('razer.device.lighting.logo', 'setBreathDual', in_sig='yyyyyy')
def set_logo_breath_dual_naga_hex_v2(self, red1, green1, blue1, red2, green2, blue2):
    """
    Set the device to dual colour breathing effect

    :param red1: Red component
    :type red1: int

    :param green1: Green component
    :type green1: int

    :param blue1: Blue component
    :type blue1: int

    :param red2: Red component
    :type red2: int

    :param green2: Green component
    :type green2: int

    :param blue2: Blue component
    :type blue2: int
    """
    self.logger.debug("DBus call set_breath_dual_effect")

    # Notify others
    self.send_effect_event('setBreathDual', red1, green1, blue1, red2, green2, blue2)

    self._write_bytes('logo_matrix_effect_breath',
                      [red1, green1, blue1, red2, green2, blue2])


@endpoint('razer.device.lighting.scroll', 'setStatic', in_sig='yyy')
def set_scroll_static_naga_hex_v2(self, red, green, blue):
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

    rgb_driver_path = self.get_driver_path('scroll_matrix_effect_static')

    self._write_bytes('scroll_matrix_effect_static', [red, green, blue])


@endpoint('razer.device.lighting.scroll', 'setSpectrum')
def set_scroll_spectrum_naga_hex_v2(self):
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

    self._write_10('scroll_matrix_effect_spectrum', 1)


@endpoint('razer.device.lighting.scroll', 'setNone')
def set_scroll_none_naga_hex_v2(self):
    """
    Set the device to spectrum mode
    """
    self.logger.debug("DBus call set_none_effect")

    # Notify others
    self.send_effect_event('setNone')

    self._write_10('scroll_matrix_effect_none', 1)


@endpoint('razer.device.lighting.scroll', 'setReactive', in_sig='yyyy')
def set_scroll_reactive_naga_hex_v2(self, red, green, blue, speed):
    """
    Set the device to reactive effect

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int

    :param speed: Speed
    :type speed: int
    """
    self.logger.debug("DBus call set_reactive_effect")

    # Notify others
    self.send_effect_event('setReactive', red, green, blue, speed)

    if speed not in (1, 2, 3, 4):
        speed = 4

    self._write_bytes('scroll_matrix_effect_reactive',
                      [speed, red, green, blue])


@endpoint('razer.device.lighting.scroll', 'setBreathRandom')
def set_scroll_breath_random_naga_hex_v2(self):
    """
    Set the device to random colour breathing effect
    """
    self.logger.debug("DBus call set_breath_random_effect")

    # Notify others
    self.send_effect_event('setBreathRandom')

    driver_path = self.get_driver_path('scroll_matrix_effect_breath')

    payload = b'1'

    self._write_bytes('scroll_matrix_effect_breath', [payload])


@endpoint('razer.device.lighting.scroll', 'setBreathSingle', in_sig='yyy')
def set_scroll_breath_single_naga_hex_v2(self, red, green, blue):
    """
    Set the device to single colour breathing effect

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_breath_single_effect")

    # Notify others
    self.send_effect_event('setBreathSingle', red, green, blue)

    driver_path = self.get_driver_path('scroll_matrix_effect_breath')

    self._write_bytes('scroll_matrix_effect_breath', [red, green, blue])


@endpoint('razer.device.lighting.scroll', 'setBreathDual', in_sig='yyyyyy')
def set_scroll_breath_dual_naga_hex_v2(self, red1, green1, blue1, red2, green2, blue2):
    """
    Set the device to dual colour breathing effect

    :param red1: Red component
    :type red1: int

    :param green1: Green component
    :type green1: int

    :param blue1: Blue component
    :type blue1: int

    :param red2: Red component
    :type red2: int

    :param green2: Green component
    :type green2: int

    :param blue2: Blue component
    :type blue2: int
    """
    self.logger.debug("DBus call set_breath_dual_effect")

    # Notify others
    self.send_effect_event('setBreathDual', red1, green1, blue1, red2, green2, blue2)

    self._write_bytes('scroll_matrix_effect_breath',
                      [red1, green1, blue1, red2, green2, blue2])
