from pydantic import BaseModel

class BaseSchema(BaseModel):
    class Coinfig:
        extra= 'forbid'
        from_attributes = True
