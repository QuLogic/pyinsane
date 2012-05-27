import sys
sys.path = ["src"] + sys.path

import unittest

import abstract
import rawapi

class TestSaneGetDevices(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_devices(self):
        devices = abstract.get_devices()
        self.assertTrue(len(devices) > 0)

    def tearDown(self):
        pass

class TestSaneOptions(unittest.TestCase):
    def setUp(self):
        devices = abstract.get_devices()
        self.assertTrue(len(devices) > 0)
        self.dev = devices[0]

    def test_get_option(self):
        val = self.dev.options['mode'].value
        self.assertNotEqual(val, None)

    def test_set_option(self):
        self.dev.options['mode'].value = "Gray"
        val = self.dev.options['mode'].value
        self.assertEqual(val, "Gray")

    def __set_opt(self, opt_name, opt_val):
        self.dev.options[opt_name].value = opt_val

    def test_set_inexisting_option(self):
        self.assertRaises(KeyError, self.__set_opt, 'xyz', "Gray")

    def test_set_invalid_value(self):
        self.assertRaises(rawapi.SaneException, self.__set_opt, 'mode', "XYZ")

    def tearDown(self):
        del(self.dev)


def get_all_tests():
    all_tests = unittest.TestSuite()

    tests = unittest.TestSuite([TestSaneGetDevices("test_get_devices")])
    all_tests.addTest(tests)

    tests = unittest.TestSuite([
        TestSaneOptions("test_get_option"),
        TestSaneOptions("test_set_option"),
        TestSaneOptions("test_set_inexisting_option"),
        TestSaneOptions("test_set_invalid_value"),
    ])
    all_tests.addTest(tests)

    return all_tests
