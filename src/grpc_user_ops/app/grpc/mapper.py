
from protobufs.protobufs_models.user_pb2 import (
    User
)
from google.protobuf.json_format import ParseDict
from google.protobuf.timestamp_pb2 import Timestamp





def map_user_entity_to_user_protos(user_dict:dict) -> User:
    user_dict['id'] = str(user_dict.get('id'))
    created_at = Timestamp()
    created_at.FromDatetime(user_dict['created_at'])
    user_dict['created_at'] = created_at.ToJsonString()
    user = User()
    ParseDict(user_dict, user)
    return user