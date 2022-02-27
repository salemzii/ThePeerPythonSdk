from http import HTTPStatus
from importlib.resources import path
import requests
import unittest
import sys
sys.path.append("..")
from ThePeer.client import Client


class TestClient(unittest.TestCase):

    _cl = Client("pssk_test_oz2rwadb7o8zp3juxb9zc3nf9ujzjmoofsqwh8u40wihm")
    def test_get_users(self) -> bool:
        path = self._cl.base_endpoint + "users"
        self._cl.set_auth_headers()
        req = self._cl.get_users()
        self.assertEqual(req.status_code, HTTPStatus.OK)

    """    def test_create_user(self):
            path = self._cl.base_endpoint + "users"
            self._cl.set_auth_headers()
            req = self._cl.create_user(data={"name":"robby", "email": "robtyler0701@gmail.com", "identifier": "robby"})
            self.assertEqual(req.status_code, HTTPStatus.CREATED)
    """
    def test_update_user(self):
        path = self._cl.base_endpoint + f"users/c00366e8-e69a-4c4d-b82a-30a4dc080bd9"
        self._cl.set_auth_headers()
        req = self._cl.update_user("c00366e8-e69a-4c4d-b82a-30a4dc080bd9", data={"identifier": "robby2"})
        self.assertEqual(req.status_code, HTTPStatus.OK)

    def test_delete_user(self):
        path = self._cl.base_endpoint + f"users/c00366e8-e69a-4c4d-b82a-30a4dc080bd9"
        self._cl.set_auth_headers()
        req = self._cl.delete_user("c00366e8-e69a-4c4d-b82a-30a4dc080bd9")
        self.assertEqual(req.status_code, HTTPStatus.OK)       

    #transactions
if __name__ == '__main':
    unittest.main()