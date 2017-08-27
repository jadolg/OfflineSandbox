import OfflineSandbox
import unittest


@OfflineSandbox.offline_sandbox_value('mundo')
def greet():
    return 'hola'


class OfflineSandboxTesting(unittest.TestCase):
    def test_no_sandbox(self):
        OfflineSandbox.SANDBOX = False
        self.assertEqual(greet(), 'hola')

    def test_sandbox(self):
        OfflineSandbox.SANDBOX = True
        self.assertEqual(greet(), 'mundo')

if __name__ == '__main__':
    unittest.main()
