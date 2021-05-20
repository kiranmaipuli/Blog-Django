Built a Blog website using Python Django 3.1.2 version

**Features of the blog:**
 - Users can Register with the Blog. 
 - Users can Login into the website
 - Registered users can write and edit the posts
 - Users can add their profile pics and edit their profile pictures

**Database:**
 - There are two models in this project.
      1) User     2) Post
 - The user model keeps track of the information about the user
 - The Post model keeps track of the each post published by each user
 - SQLLite which comes along with Django framework is used as the database in this project


**Apps:**
  - The website consists of two apps - blog and users
    Users app:
      - users app deals with the register, login, editing profile, password reset functionality
      - Crispy forms of Django framework is utilized for creating register and login forms
    Blog app:
      - Blog app deals with creating and editing of user posts, keeping count of the posts of each user and pagination of the posts
