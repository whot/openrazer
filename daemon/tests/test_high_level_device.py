import unittest

import openrazer_daemon.device

DEVICE1_SERIAL = 'XX000000'
DEVICE1_ID = '0000:0000:0000.0000'

DEVICE2_SERIAL = 'XX000001'
DEVICE2_ID = '0000:0000:0000.0001'

class DummyDBusObject(object):
    def __init__(self):
        self.notify_msg = None
        self.parent = None

    def notify(self, msg):
        self.notify_msg = msg

    def register_parent(self, parent):
        self.parent = parent

    def notify_parent(self, msg):
        self.parent.notify_parent(msg)

class DummyParentObject(object):
    def __init__(self):
        self.notify_msg = None
        self.notify_device = None

    def notify(self, device_object, msg):
        self.notify_device = device_object
        self.notify_msg = msg

# TODO move device_object creation to setUp
class DeviceTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_device_properties(self):
        dbus_object = DummyDBusObject()
        device_object = openrazer_daemon.device.Device(DEVICE1_ID, DEVICE1_SERIAL, dbus_object)

        self.assertEqual(device_object.device_id, DEVICE1_ID)
        self.assertEqual(device_object.serial, DEVICE1_SERIAL)
        self.assertEqual(device_object.dbus, dbus_object)

    def test_device_register_parent(self):
        dbus_object = DummyDBusObject()
        parent_object = DummyParentObject()

        device_object = openrazer_daemon.device.Device(DEVICE1_ID, DEVICE1_SERIAL, dbus_object)
        device_object.register_parent(parent_object)

        self.assertEqual(device_object._parent, parent_object)

    def test_device_notify_child(self):
        msg = ('test', 1)

        dbus_object = DummyDBusObject()

        device_object = openrazer_daemon.device.Device(DEVICE1_ID, DEVICE1_SERIAL, dbus_object)
        device_object.notify_child(msg)

        self.assertEqual(dbus_object.notify_msg, msg)

    def test_device_notify_parent(self):
        msg = ('test', 1)

        dbus_object = DummyDBusObject()
        parent_object = DummyParentObject()

        device_object = openrazer_daemon.device.Device(DEVICE1_ID, DEVICE1_SERIAL, dbus_object)
        device_object.register_parent(parent_object)

        device_object.notify_parent(msg)

        self.assertEqual(parent_object.notify_msg, msg)
        self.assertEqual(parent_object.notify_device, device_object)

