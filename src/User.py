class User:

  ID_user_code: str
  name: str
  email: str
  password: str

  def __init__(self,ID_user_code,name,email,password):
    self.ID_user_code = ID_user_code
    self.name = name
    self.email = email
    self.password = password