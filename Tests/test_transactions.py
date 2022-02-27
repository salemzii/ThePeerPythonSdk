from http import HTTPStatus
from importlib.resources import path
import requests
import unittest
import sys
sys.path.append("..")
from ThePeer.client import Client


class TestTransactions(unittest.TestCase):

    _cl = Client("PRIVATE_KEY")

    def test_transaction(self):
        path = self._cl.base_endpoint + "transactions/TRANSACTIONID"
        self._cl.set_auth_headers()
        req = self._cl.get_transaction()
        self.assertEqual(req.status_code, HTTPStatus.OK)
