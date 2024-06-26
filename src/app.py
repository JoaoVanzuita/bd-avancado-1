import boto3
from boto3.dynamodb.conditions import Key
from User import User
from Cart import Cart

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id='dummy',
                          aws_secret_access_key='dummy',
                          region_name='us-west-2',
                          endpoint_url='http://localhost:8000')

##----------- CREATE TABLE CART -----------##

def create_table_cart():
  dynamodb.create_table(
    TableName='Cart',
    AttributeDefinitions=[
      {
        'AttributeName': 'ID_cart_code',
        'AttributeType': 'S'
      }
    ],
    KeySchema=[
      {
        'AttributeName': 'ID_cart_code',
        'KeyType':'HASH'
      }
    ],
    ProvisionedThroughput={
      'ReadCapacityUnits': 5,
      'WriteCapacityUnits': 5
    }
  )

##----------- CREATE TABLE USER -----------##

def create_table_user():
  dynamodb.create_table(
    TableName='User',
    KeySchema=[
      {
        'AttributeName': 'ID_user_code',
        'KeyType': 'HASH'
      }
    ],
    AttributeDefinitions=[
      {
        'AttributeName': 'ID_user_code',
        'AttributeType': 'S'
      }
    ],
    ProvisionedThroughput={
      'ReadCapacityUnits': 5,
      'WriteCapacityUnits': 5
    }
  )

##----------- INSERT USER -----------##

def insert_user(user):
  table = dynamodb.Table('User')

  table.put_item(
    Item = {
      'ID_user_code': user.ID_user_code,
      'name': user.name,
      'email': user.email,
      'password': user.password
    }
  )

##----------- INSERT CART -----------##

def insert_cart(cart):
  table = dynamodb.Table('Cart')

  table.put_item(
    Item = {
      'ID_cart_code': cart.ID_cart_code,
      'date': cart.date,
      'items': cart.items,
      'user_REF': cart.user_REF
    }
  )

##----------- READ CART -----------##

def select_cart(cart):
    table = dynamodb.Table('Cart')

    result = table.query(
      KeyConditionExpression=Key('ID_cart_code').eq(cart.ID_cart_code)
    )

    print(result['Items'])

##----------- UPDATE USER -----------##

def update_user(user):
  table = dynamodb.Table('User')

  table.update_item(
    Key={
      'ID_user_code': user.ID_user_code
    },
    UpdateExpression='SET email = :newval',
    ExpressionAttributeValues={
      ':newval': user.email
    },
    ReturnValues='ALL_NEW'
  )

##----------- DELETE CART -----------##

def delete_cart(id_cart):
  table = dynamodb.Table('Cart')

  table.delete_item(
    Key={
      'ID_cart_code': id_cart
    }
  )


##----------- TESTS -----------##

user1 = User(
  ID_user_code='3308fa75b710f5979103f9ad37e8a9b3',
  name='Joao',
  email='joao@gmail.com',
  password='9827de0adaae57d74965748528114009'
)

cart1 = Cart(
  ID_cart_code='e7ce808fb1ab22af259264997a8c72c6',
  date='2024-06-25',
  items=[
    {'name':'produto', 'unit_value':10, 'quantity':2}
  ],
  user_REF=user1.ID_user_code
)

create_table_cart()
create_table_user()

insert_user(user1)
insert_cart(cart1)

select_cart(cart1)

user1.email = 'joao-editado@gmail.com'

update_user(user1)

delete_cart(cart1.ID_cart_code)