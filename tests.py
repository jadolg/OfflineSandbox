import OfflineSandbox
import unittest


@OfflineSandbox.offline_sandbox_value('mundo')
def greet():
    return 'hola'


@OfflineSandbox.offline_sandbox_value('mundo', url='https://im-online.herokuapp.com/')
def greet_with_url():
    return 'hola'


class OfflineSandboxTesting(unittest.TestCase):
    def test_no_sandbox(self):
        OfflineSandbox.SANDBOX = False
        self.assertEqual(greet(), 'hola')

    def test_sandbox(self):
        OfflineSandbox.SANDBOX = True
        self.assertEqual(greet(), 'mundo')

    def test_sandbox_url(self):
        self.assertEqual(greet_with_url(), 'hola')

if __name__ == '__main__':
    unittest.main()
