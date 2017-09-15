"""
BlackWidow Chroma Effects
"""
import os
from openrazer_daemon.dbus_services import endpoint


@endpoint('razer.device.lighting.brightness', 'getBrightness', out_sig='d')
def get_brightness(self):
    """
    Get the device's brightness

    :return: Brightness
    :rtype: float
    """
    self.logger.debug("DBus call get_brightness")

    brightness = self._read_percent('matrix_brightness', maxval=255)
    self.cached_values['brightness'] = brightness

    return brightness


@endpoint('razer.device.lighting.brightness', 'setBrightness', in_sig='d')
def set_brightness(self, brightness):
    """
    Set the device's brightness

    :param brightness: Brightness
    :type brightness: int
    """
    self.logger.debug("DBus call set_brightness")

    self.cached_values['brightness'] = brightness
    brightness = self._write_percent('matrix_brightness', brightness, maxval=255)

    # Notify others
    self.send_effect_event('setBrightness', brightness)


@endpoint('razer.device.led.gamemode', 'getGameMode', out_sig='b')
def get_game_mode(self):
    """
    Get game mode LED state

    :return: Game mode LED state
    :rtype: bool
    """
    self.logger.debug("DBus call get_game_mode")

    return self._read_10('game_led_state')


@endpoint('razer.device.led.gamemode', 'setGameMode', in_sig='b')
def set_game_mode(self, enable):
    """
    Set game mode LED state

    :param enable: Status of game mode
    :type enable: bool
    """
    self.logger.debug("DBus call set_game_mode")

    driver_path = self.get_driver_path('game_led_state')

    for kb_int in self.additional_interfaces:
        super_file = os.path.join(kb_int, 'key_super')
        alt_tab = os.path.join(kb_int, 'key_alt_tab')
        alt_f4 = os.path.join(kb_int, 'key_alt_f4')

        if enable:
            open(super_file, 'wb').write(b'\x01')
            open(alt_tab, 'wb').write(b'\x01')
            open(alt_f4, 'wb').write(b'\x01')
        else:
            open(super_file, 'wb').write(b'\x00')
            open(alt_tab, 'wb').write(b'\x00')
            open(alt_f4, 'wb').write(b'\x00')

    self._write_10('game_led_state', enable)


@endpoint('razer.device.led.macromode', 'getMacroMode', out_sig='b')
def get_macro_mode(self):
    """
    Get macro mode LED state

    :return: Status of macro mode
    :rtype: bool
    """
    self.logger.debug("DBus call get_macro_mode")

    return self._read_10('macro_led_state')


@endpoint('razer.device.led.macromode', 'setMacroMode', in_sig='b')
def set_macro_mode(self, enable):
    """
    Set macro mode LED state

    :param enable: Status of macro mode
    :type enable: bool
    """
    self.logger.debug("DBus call set_macro_mode")

    self._write_10('macro_led_state', enable)


@endpoint('razer.device.led.macromode', 'getMacroEffect', out_sig='i')
def get_macro_effect(self):
    """
    Get the effect on the macro LED

    :return: Macro LED effect ID
    :rtype: int
    """
    self.logger.debug("DBus call get_macro_effect")

    return self._read_int('macro_led_effect')


@endpoint('razer.device.led.macromode', 'setMacroEffect', in_sig='y')
def set_macro_effect(self, effect):
    """
    Set the effect on the macro LED

    :param effect: Macro LED effect ID
    :type effect: int
    """
    self.logger.debug("DBus call set_macro_effect")

    self._write_int('macro_led_effect')


@endpoint('razer.device.lighting.chroma', 'setWave', in_sig='i')
def set_wave_effect(self, direction):
    """
    Set the wave effect on the device

    :param direction: 1 - left to right, 2 right to left
    :type direction: int
    """
    self.logger.debug("DBus call set_wave_effect")

    # Notify others
    self.send_effect_event('setWave', direction)

    if direction not in self.WAVE_DIRS:
        direction = self.WAVE_DIRS[0]

    self._write_string('matrix_effect_wave', direction)


@endpoint('razer.device.lighting.chroma', 'setStatic', in_sig='yyy')
def set_static_effect(self, red, green, blue):
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

    self._write_bytes('matrix_effect_static', [red, green, blue])


@endpoint('razer.device.lighting.chroma', 'setBlinking', in_sig='yyy')
def set_blinking_effect(self, red, green, blue):
    """
    Set the device to static colour

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int
    """
    self.logger.debug("DBus call set_blinking_effect")

    # Notify others
    self.send_effect_event('setBlinking', red, green, blue)

    self._write_bytes('matrix_effect_blinking', [red, green, blue])


@endpoint('razer.device.lighting.chroma', 'setSpectrum')
def set_spectrum_effect(self):
    """
    Set the device to spectrum mode
    """
    self.logger.debug("DBus call set_spectrum_effect")

    # Notify others
    self.send_effect_event('setSpectrum')

    self._write_10('matrix_effect_spectrum', 1)


@endpoint('razer.device.lighting.chroma', 'setNone')
def set_none_effect(self):
    """
    Set the device to spectrum mode
    """
    self.logger.debug("DBus call set_none_effect")

    # Notify others
    self.send_effect_event('setNone')

    self._write_10('matrix_effect_none', 1)


@endpoint('razer.device.misc', 'triggerReactive')
def trigger_reactive_effect(self):
    """
    Trigger reactive on Firefly
    """
    self.logger.debug("DBus call trigger_reactive_effect")

    # Notify others
    self.send_effect_event('triggerReactive')

    self._write_10('matrix_reactive_trigger', 1)


@endpoint('razer.device.lighting.chroma', 'setReactive', in_sig='yyyy')
def set_reactive_effect(self, red, green, blue, speed):
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

    self._write_bytes('matrix_effect_reactive', [speed, red, green, blue])


@endpoint('razer.device.lighting.chroma', 'setBreathRandom')
def set_breath_random_effect(self):
    """
    Set the device to random colour breathing effect
    """
    self.logger.debug("DBus call set_breath_random_effect")

    # Notify others
    self.send_effect_event('setBreathRandom')


    self._write_bytes('matrix_effect_breath', [1])


@endpoint('razer.device.lighting.chroma', 'setBreathSingle', in_sig='yyy')
def set_breath_single_effect(self, red, green, blue):
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

    self._write_bytes('matrix_effect_breath', [red, green, blue])


@endpoint('razer.device.lighting.chroma', 'setBreathTriple', in_sig='yyyyyyyyy')
def set_breath_triple_effect(self, red1, green1, blue1, red2, green2, blue2, red3, green3, blue3):
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

    :param red3: Red component
    :type red3: int

    :param green3: Green component
    :type green3: int

    :param blue3: Blue component
    :type blue3: int
    """
    self.logger.debug("DBus call set_breath_dual_effect")

    # Notify others
    self.send_effect_event('setBreathDual', red1, green1, blue1, red2, green2, blue2, red3, green3, blue3)

    self._write_bytes('matrix_effect_breath',
                      [red1, green1, blue1, red2, green2, blue2, red3, green3, blue3])


@endpoint('razer.device.lighting.chroma', 'setBreathDual', in_sig='yyyyyy')
def set_breath_dual_effect(self, red1, green1, blue1, red2, green2, blue2):
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

    self._write_bytes('matrix_effect_breath',
                      [red1, green1, blue1, red2, green2, blue2])


@endpoint('razer.device.lighting.chroma', 'setCustom')
def set_custom_effect(self):
    """
    Set the device to use custom LED matrix
    """
    # TODO uncomment
    # self.logger.debug("DBus call set_custom_effect")

    self._write_bytes('matrix_effect_custom', [1])


@endpoint('razer.device.lighting.chroma', 'setKeyRow', in_sig='ay', byte_arrays=True)
def set_key_row(self, payload):
    """
    Set the RGB matrix on the device

    Byte array like
    [1, 255, 255, 00, 255, 255, 00, 255, 255, 00, 255, 255, 00, 255, 255, 00, 255, 255, 00, 255, 255, 00, 255, 255, 00,
        255, 255, 00, 255, 255, 00, 255, 255, 00, 255, 255, 00, 255, 255, 00, 255, 255, 00, 255, 00, 00]

    First byte is row, on firefly its always 1, on keyboard its 0-5
    Then its 3byte groups of RGB
    :param payload: Binary payload
    :type payload: bytes
    """

    # TODO uncomment
    # self.logger.debug("DBus call set_key_row")

    self._write_bytes('matrix_custom_frame', payload)


@endpoint('razer.device.lighting.custom', 'setRipple', in_sig='yyyd')
def set_ripple_effect(self, red, green, blue, refresh_rate):
    """
    Set the daemon to serve a ripple effect of the specified colour

    :param red: Red component
    :type red: int

    :param green: Green component
    :type green: int

    :param blue: Blue component
    :type blue: int

    :param refresh_rate: Refresh rate
    :type refresh_rate: int
    """
    self.logger.debug("DBus call set_ripple_effect")

    # Notify others
    self.send_effect_event('setRipple', red, green, blue, refresh_rate)


@endpoint('razer.device.lighting.custom', 'setRippleRandomColour', in_sig='d')
def set_ripple_effect_random_colour(self, refresh_rate):
    """
    Set the daemon to serve a ripple effect of random colours

    :param refresh_rate: Refresh rate
    :type refresh_rate: int
    """
    self.logger.debug("DBus call set_ripple_effect")

    # Notify others
    self.send_effect_event('setRipple', None, None, None, refresh_rate)


@endpoint('razer.device.lighting.chroma', 'setStarlightRandom', in_sig='y')
def set_starlight_random_effect(self, speed):
    """
    Set startlight random mode
    """
    self.logger.debug("DBus call set_starlight_random")

    self._write_bytes('matrix_effect_starlight', [speed])

    # Notify others
    self.send_effect_event('setStarlightRandom')


@endpoint('razer.device.lighting.chroma', 'setStarlightSingle', in_sig='yyyy')
def set_starlight_single_effect(self, speed, red, green, blue):
    """
    Set starlight mode
    """
    self.logger.debug("DBus call set_starlight_single")

    self._write_bytes('matrix_effect_starlight', [speed, red, green, blue])

    # Notify others
    self.send_effect_event('setStarlightSingle', speed, red, green, blue)


@endpoint('razer.device.lighting.chroma', 'setStarlightDual', in_sig='yyyyyyy')
def set_starlight_dual_effect(self, speed, red1, green1, blue1, red2, green2, blue2):
    """
    Set starlight dual mode
    """
    self.logger.debug("DBus call set_starlight_dual")

    self._write_bytes('matrix_effect_starlight',
                      [speed, red1, green1, blue1, red2, green2, blue2])

    # Notify others
    self.send_effect_event('setStarlightDual', speed, red1, green1, blue1)
