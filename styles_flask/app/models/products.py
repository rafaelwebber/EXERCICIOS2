from pydantic import AliasChoices, BaseModel, Field, ConfigDict
from typing import Optional
from bson import ObjectId

class Product(BaseModel):
    id: Optional[ObjectId] = Field(None, alias='_id')
    name: str
    prices: float = Field(validation_alias=AliasChoices('prices', 'price'))
    description: Optional[str] = None
    stock: int
    sku: str #sku = 

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )

class ProductDBMondel(Product):
    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)
        if self.id:
            data['_id'] = str(data['_id'])
        return data

