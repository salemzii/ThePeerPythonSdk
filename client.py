from dataclasses import dataclass
import requests
import json
from validators import Validator
from schema_conf import (create_user_schema_conf, 
                            update_user_schema_conf,
                            transaction_refund_schema_conf,
                            test_recieve_schema_conf,
                            charge_schema_conf,)

@dataclass
class Client():

    api_key : str
    

    request = requests.Session()
    base_endpoint = "https://api.thepeer.co/"

    def set_auth_headers(self):
        headers = {
            "X-Api-Key": self.api_key,
            "Accept": "application/json"
        }
        return self.request.headers.update(headers)

    
    def get_users(self) -> dict:
        path = self.base_endpoint + "users"
        self.set_auth_headers()
        try:
            req = self.request.get(path)
            return json.loads(req.text)
        except Exception as err:
            return err

    
    def create_user(self, data : dict) -> dict:
        path = self.base_endpoint + "users"
        self.set_auth_headers()

        if Validator(data, create_user_schema_conf).validate():
            try:
                req = self.request.post(path, data=data)
                return json.loads(req.text)
            except Exception as err:
                return err
        else:
            raise "invalid post data"
    

    def update_user(self, reference:str, data:dict) -> dict:
        
        path = self.base_endpoint + f"users/{reference}"
        self.set_auth_headers()
        if Validator(data, update_user_schema_conf).validate():
            try:
                req = self.request.put(path, data=data)
                return json.loads(req.text)
            except Exception as err:
                return err
        else:
            raise "invalid post data"
    
    def delete_user(self, reference:str) -> dict:
        path = self.base_endpoint + f"users/{reference}"
        self.set_auth_headers()
        try:
            req = self.request.delete(path)
            return json.loads(req.text)
        except Exception as err:
            return err             


    """
        transaction records Get a transaction by it's id
    """

    def get_transaction(self, transactionId) -> dict:

        path = self.base_endpoint +f"transactions/{transactionId}"
        self.set_auth_headers()
        try:
            req = self.request.get(path)
            return json.loads(req.text)
        except Exception as err:
            return err

    def refund_transaction(self, transactionId, data=None) -> json:
        path = self.base_endpoint +f"transactions/{transactionId}/refund"
        self.set_auth_headers()

        try:
            if data != None and Validator(data, transaction_refund_schema_conf):
                req = self.request.post(path, data=data)
                return json.loads(req.text)
            req = self.request.post(path, data={"reason":"possible fraud"})
            return json.loads(req.text)
        except Exception as err:
            return err

    def get_user_links(self, reference: str) -> json:
        path = self.base_endpoint + f"users/{reference}/links"
        self.set_auth_headers()

        try:
            req = self.request.get(path)
            return json.loads(req.text)

        except Exception as err:
            return err

    def get_user_link(self, linkId: str) -> json:
        path = self.base_endpoint + f"link/{linkId}"
        self.set_auth_headers()

        try:
            req = self.request.get(path)
            return json.loads(req.text)
        except Exception as err:
            return err

    def test_recieve(self, data=None) -> json:
        path = self.base_endpoint + f"test-receive"
        self.set_auth_headers()

        try:
            if data != None and Validator(data, test_recieve_schema_conf).validate():
                req = self.request.post(path,data=data)
                print(type(req.text))
                return json.loads(req.text)
            req = self.request.post(path, data={ "amount": 10000,"user_reference": "banana-island-ikoyi"})
            return req.text
        except Exception as err:
            return err
    

    def charge(self, linkId:str, data:dict) -> json:
        path = self.base_endpoint + f"link/{linkId}/charge"

        if Validator(data, charge_schema_conf).validate():
            try:
                req = self.request.post(path, data=data)
                return json.loads(req.text)
            except Exception as err:
                return err
        else:
            raise "Invalid Post data"

    
c = Client("pssk_test_oz2rwadb7o8zp3juxb9zc3nf9ujzjmoofsqwh8u40wihm")
r = "c33e73e4-8c7d-4459-94ce-07056603790d"
print(c.get_user_links(r))
#print(c.test_recieve())