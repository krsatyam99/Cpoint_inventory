# Cpoint5 Inventory
A simple Django rest Api Project having 4 endpoints performing the crud operation. \
Mainly 2 end points Create and list the inventory's items.


## Requirements:
Python \
Django \
Django rest Framework \
PILLOW 
#####  You can install them from pip install -r requirements.txt 

## Installation 

###### 1. Clone the project
git clone https://github.com/krsatyam99/Cpoint_inventory.git

###### 2. Install dependencies
pip install -r requirements.txt

###### 3. Apply database migrations
python manage.py makemigrations
python manage.py migrate



###### 4. Create a superuser (admin user)
python manage.py createsuperuser

###### 5. Run the development server
python manage.py runserver

## Endpoints 
#### main 
###### http://127.0.0.1:8000/inventory/grocery/
![Screenshot (37)](https://github.com/krsatyam99/Cpoint_inventory/assets/103446420/2a469799-c0e4-4ec0-9f34-dd897303bff2)

###### http://127.0.0.1:8000/inventory/grocery_list/
![Screenshot (38)](https://github.com/krsatyam99/Cpoint_inventory/assets/103446420/10bde65f-23a1-43b1-970b-4a752d5fd916)

#### Additional 
###### http://127.0.0.1:8000/inventory/grocery/<int:pk>/delete/ 
![Screenshot (44)](https://github.com/krsatyam99/Cpoint_inventory/assets/103446420/8a0b56d1-4188-4c3b-af5c-768d9a23ccb0)


###### http://127.0.0.1:8000/inventory/<int:pk>/update/
![Screenshot (43)](https://github.com/krsatyam99/Cpoint_inventory/assets/103446420/d69e37b1-8ef8-4cd6-b660-83247377cebf)


###### http://127.0.0.1:8000/admin/inventory/groceryitem/

![Screenshot (39)](https://github.com/krsatyam99/Cpoint_inventory/assets/103446420/49d31a97-49d5-44f6-821c-a86fbc260885)


## Genericviews and types used in the project
In Django REST Framework (DRF), generic views are a set of pre-built class-based views that provide common patterns for performing CRUD (Create, Retrieve, Update, Delete) operations on models. These generic views help in reducing code duplication and boilerplate by providing a standardized way to handle common actions.
### generics.CreateAPIView
In Django REST Framework (DRF), generics.CreateAPIView is a class-based view that provides a generic implementation for creating a new object.
Purpose: Used for handling HTTP POST requests to create a new object.
Inheritance: Inherits from generics.GenericAPIView and mixins.CreateModelMixin.
### generics.RetrieveAPIView
In Django REST Framework (DRF), generics.RetrieveAPIView is a class-based view that provides a generic implementation for retrieving a single object.
Purpose: Used for handling HTTP GET requests to retrieve a single object based on its primary key.
Inheritance: Inherits from generics.GenericAPIView and mixins.RetrieveModelMixin.
### generics.ListAPIView
In Django REST Framework (DRF), generics.ListAPIView is a class-based view that provides a generic implementation for retrieving a list of objects.
Purpose: Used for handling HTTP GET requests to retrieve a list of objects.
Inheritance: Inherits from generics.GenericAPIView and mixins.ListModelMixin.
### generics.UpdateAPIView
In Django REST Framework (DRF), generics.UpdateAPIView is a class-based view that provides a generic implementation for updating a single object.
Purpose: Used for handling HTTP PUT and PATCH requests to update a single object based on its primary key.
Inheritance: Inherits from generics.GenericAPIView and mixins.UpdateModelMixin.
### generics.DestroyAPIView
Used for delete-only endpoints for a single model instance.

Provides a delete method handler.

Extends: GenericAPIView, DestroyModelMixin

#### Thanks and Regards
Kumar Satyam
https://www.linkedin.com/in/kumar-satyam-769340243/
