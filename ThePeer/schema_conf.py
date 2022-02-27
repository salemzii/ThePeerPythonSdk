from .validators import Validator
from schema import Schema, And, Use, Optional, SchemaError

create_user_schema_conf  = Schema({
    'name': And(Use(str)),
    'identifier': And(Use(str)),
    'email': And(Use(str))
})

update_user_schema_conf = Schema({
    'identifier': And(Use(str))
})

transaction_refund_schema_conf = Schema({
    "reason" : And(Use(str))
})

test_recieve_schema_conf = Schema({
    "amount": And(Use(int)),
    "user_reference": And(Use(str))
})

charge_schema_conf = Schema({
    "amount": And(Use(str)),
    "remark": And(Use(str))
})


d = {
    "name": "david bill",
    "identifier": "david",
    "email": "davidbill0701@gmail.com"
}
dd = {"reason":"robby2"}

v = Validator(dd, transaction_refund_schema_conf)
print(v.validate())