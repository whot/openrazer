"""
Class to hold a device and collections of them
"""


class Device(object):
    """
    Razer Device (High level not dbus)
    """
    def __init__(self, device_id, device_serial, device_dbus_object):
        self._parent = None

        self._id = device_id
        self._serial = device_serial
        self._dbus = device_dbus_object
        # Register as parent
        self._dbus.register_parent(self)

    @property
    def device_id(self):
        """
        Device's USB ID String

        :return: Device ID
        :rtype: str
        """
        return self._id
    @property
    def serial(self):
        """
        Device's Serial String

        :return: Serial
        :rtype: str
        """
        return self._serial
    @property
    def dbus(self):
        """
        Device's DBus object

        :return: DBus Object
        :rtype: openrazer_daemon.hardware.device_base.__RazerDevice
        """
        return self._dbus

    def register_parent(self, parent):
        """
        Register the parent as an observer to be optionally notified (sends to other devices)

        :param parent: Observer
        :type parent: object
        """
        self._parent = parent

    def notify_parent(self, msg):
        """
        Notify observers with msg

        :param msg: Tuple with first element a string
        :type msg: tuple
        """
        self._parent.notify(self, msg)

    def notify_child(self, msg):
        """
        Receive observer messages

        :param msg: Tuple with first element a string
        :type msg: tuple
        """
        # Message from DBus object
        self._dbus.notify(msg)

