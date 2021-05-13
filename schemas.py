from pydantic import BaseModel

class independent(BaseModel):
    variance:float
    skewness:float
    curtosis:float
    entropy:float
    
    
