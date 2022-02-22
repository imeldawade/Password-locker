from credential import Credential
import unittest

class TestCredentials(unittest.TestCase):
    def test_init(self):
        '''
        creates 
        '''
        self.assertEqual(self.new_credential.site, 'email')
        self.assertEqual(self.new_credential.site, '15802')