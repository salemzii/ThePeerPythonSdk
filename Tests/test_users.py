from http import HTTPStatus
from importlib.resources import path
import requests
import unittest
import sys
sys.path.append("..")
from ThePeer.client import Client


class TestUsers(unittest.TestCase):

    _cl = Client("PRIVATE_KEY")
    def test_get_users(self) -> bool:
        path = self._cl.base_endpoint + "users"
        self._cl.set_auth_headers()
        req = self._cl.get_users()
        self.assertEqual(req.status_code, HTTPStatus.OK)

    def test_create_user(self):
        path = self._cl.base_endpoint + "users"
        self._cl.set_auth_headers()
        req = self._cl.create_user(data={"name":"", "email": "", "identifier": ""})
        self.assertEqual(req.status_code, HTTPStatus.CREATED)

    def test_update_user(self):
        path = self._cl.base_endpoint + f"users/REFERENCEID"
        self._cl.set_auth_headers()
        req = self._cl.update_user("REFERENCEID", data={"identifier": ""})
        self.assertEqual(req.status_code, HTTPStatus.OK)

    def test_delete_user(self):
        path = self._cl.base_endpoint + f"users/REFERENCEID"
        self._cl.set_auth_headers()
        req = self._cl.delete_user("REFERENCEID")
        self.assertEqual(req.status_code, HTTPStatus.OK)       

    #transactions
if __name__ == '__main':
    unittest.main()