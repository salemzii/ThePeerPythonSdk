from validators import Validator
from schema import Schema, And, Use, Optional, SchemaError

create_user_schema_conf  = Schema({
    'name': And(Use(str)),
    'identifier': And(Use(str)),
    'email': And(Use(str))
})

update_user_schema_conf = Schema({
    'identifier': And(Use(str))
})


d = {
    "name": "david bill",
    "identifier": "david",
    "email": "davidbill0701@gmail.com"
}
dd = {"identifier":"robby2"}

v = Validator(dd, update_user_schema_conf)
print(v.validate())