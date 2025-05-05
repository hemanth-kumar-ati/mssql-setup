from sqlalchemy import Column, Integer, String
from config.database import Base
import json
from sqlalchemy.types import TypeDecorator, Text
class JSONEncodedArray(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        if value is not None:
            return json.dumps(value)
        return None

    def process_result_value(self, value, dialect):
        if value is not None:
            return json.loads(value)
        return None



class User(Base):
    __tablename__ = 'Users'
    
    Id = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False, unique=True)
    scores = Column(JSONEncodedArray, nullable=True)
    movies_watched = Column(JSONEncodedArray, nullable=True)

