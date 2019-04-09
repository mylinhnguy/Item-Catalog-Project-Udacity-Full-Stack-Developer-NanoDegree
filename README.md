
# Item Catalog Project

## Project Overview
Develop a RESTful web application that provides a list of items within a variety of categories as well as provide a user registration and authentication system.
Registered users will have the ability to post, edit and delete their own items.
The web app is built using the Python framework Flask and used SQLAlchemy to interface with an SQLite database using object-relational mapping (ORM) 
along with implementing third-party OAuth authentication.
Efficiently interacting with data is the backbone upon which performant web applications are built.
Properly implementing authentication mechanisms and appropriately mapping HTTP methods to CRUD operations are core features of a properly secured web application

## Features
* Implement CRUD (create, read, update, delete) operations
* Build forms for user input
* Perform client side and server side input validation
* Implement third-party OAuth2 authentication using Google Sign-in API.
* Proper authentication and authorization check.
* The web has protection against cross-site request forgery (CSRF) attacks by using the Flask plugin SeaSurf. 
* Create and interact with SQLite database using SQLAlchemy
* JSON endpoints.

## Skills 
1. Python
2. HTML
3. CSS
4. OAuth2 authentication
5. Flask Framework
6. SQLite database
7. SQLAlchemy
8. Google Login 

## Project Structure 

```          
  |-- project.py 
  |-- client_secrets.json
  |-- database_setup.py 
  |-- lotsofitems.py
  |-- catalog.db 
  |-- LICENSE 
  |-- README.md 
  |-- /static 
      |-- style.css 
  |-- /Templates 
      |-- catalog.html 
      |-- category.html 
      |-- deleteitem.html
      |-- edititem.html 
      |-- footer.html 
      |-- header.html 
      |-- item.html
      |-- login.html 
      |-- newitem.html 
      |-- publiccatalog.html
      |-- publicitem.html 
```

## Setting up OAuth2.0 using Google Login

```
* To get third-party OAuth2 authentication using Google Sign-in API working there are a few additional steps:
* Sign up to Google account 
* [Visit https://console.developers.google.com]( https://console.developers.google.com ) 
* Sign in with Google account to get a **client_id and client_secret** 
* Go to Credentials 
* Select Web application 
* Enter name 'ItemCatalogHair' 
* Authorized JavaScript origins = 'http://localhost:8000' 
* Authorized redirect URIs = 'http://localhost:8000/login' && 'http://localhost:8000/gconnect' 
* Select Create 
* Copy the Client ID and paste it into the data-clientid in login.html 
* On the Dev Console Select Download JSON 
* Rename JSON file to client_secrets.json 
* Place JSON file in ItemCatalogHair directory that you cloned from here 
```

## How to Run
### PreRequisites:

```
    Python3 
    VirtualBox 
    Vagrant
    QLite database
    SQLAlchemy 
```
## Setup Project:
1. Download and install Python 3.7
2. Download and install VirtualBox 
3. Download and install Vagrant
4. Download and install Git Bash terminal
5. Download or Clone fullstack-nanodegree-vm repository. https://github.com/udacity/fullstack-nanodegree-vm

## Launching the Virtual Machine: 
1. Launch the Vagrant VM  

   ```
   $ vagrant up
   ```
2. Log into this using command

   ```
   $ vagrant ssh
   ```
3. Change directory to the /vagrant directory by typing
   
   ```
   $ cd /vagrant and ls
   ```

## Setting up the database and run web application :
1. SQL database is created using the database_setup.py: 

   ```
   $ python database_setup.py
   ```
2. Load the data in local database using the command: 

   ```
   $ python lotsofitems.py   
   ```
3. Run web application 

   ```
   $ python project.py 
   ```
4. Open your web browser and visit http://localhost:8000

6. The web page will open and you will need to click on login and then use Google+  to login.

## The database includes three tables: 

  ```
    1.  The User table includes information about the users. <br />
    2.  The Categories table includes the catagories of web application. <br />
    3.  The CategoryItem table includes name, description and url_image. <br />
    Data loaded successfully with message "added items into categories!"
  ```

## JSON Endpoints

```

**/catalog/JSON - Returns JSON of all catalog**  
 ![CatalogJSON](gif/jsonImage/CatalogJSON.PNG)  

**/catalog/categories/JSON - Returns JSON of all categories in catalog**  
  ![CategoriesJSON](gif/jsonImage/CategoriesJSON.PNG)

**/catalog/<int:categories_id>/JSON - Returns JSON of selected category in catalog**  
  ![SpecificCategory](gif/jsonImage/SpecificCategory.PNG)

**/catalog/<int:categories_id>/<int:items_id>/JSON - Returns JSON of selected item in catalog>**  
 ![SpecificItem](gif/jsonImage/SpecificItem.PNG)
```
 


















