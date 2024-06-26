from typing import Dict, List, Union

class Cart:
  ID_cart_code: str
  date: str
  items: List[Dict[str, Union[str, float, int]]]
  user_REF: str

  def __init__(self,ID_cart_code,date,items,user_REF):
    self.ID_cart_code = ID_cart_code
    self.date = date
    self.items = items
    self.user_REF = user_REF