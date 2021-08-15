from uuid import uuid4

def gen_uuid() -> str:
    """
        Return a str representation of a uuid4
    """
    return str(uuid4())


from .articles import *
from .authors import *