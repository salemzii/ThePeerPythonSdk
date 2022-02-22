from dataclasses import dataclass
import requests
import json
from validators import Validator
from schema_conf import (create_user_schema_conf, 
                            update_user_schema_conf)

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