# Menooh - Cookbook Building Website
<img src="static/media/responsive.png" ><br>
<hr>

## Overview
This project is designed and developed to help users create and manage their own recipe books for cooking at home. Think Pinterest for foodies. The users are given the option to create their own recipes, add recipes from other users to their own cookbook collections, furnish their own user profile, and leave comments on other recipes. All these functionalities are available to any user with an account. <br>
The website was created for domestic users, but there is no reason that businesses wouldn't also use it. This is a working demonstration of this site model which has the potential to be scaled to a functioning business in it's own right. <br>
**Menooh - cookbook building website** was developed using Python (Django), HTML, CSS and JavaScript by storing the data in a PostgreSQL database.
<br><br>
The fully deployed project can be accessed at [this link](https://menooh-49c095ee8d82.herokuapp.com/).<br><br>

## UX
This site was created respecting the Five Planes Of Website Design:<br>
### Strategy<hr>
**User Stories:** <br>

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**CONTENT AND NAVIGATION**             |  ||
|                                       |1A| As a user, I want to see a nav menu so I can easily navigate through website content|
|                                       |1B| As a user, I want to understand the purpose of the site|
|                                       |1C| As a user, I want the website to have a nice and intuitive design which I recognise|
|**USER REGISTRATION/AUTENTHICATION**   |  ||
|                                       |2A| As a user, I want to be able to register on the website|
|                                       |2B| As a user, I want to be able to authenticate using only email and password|
|                                       |2C| As a user, I want to be able to log out at any time|
|**COOKBOOKS**                          |  ||
|                                       |3A| As a logged-in user, I want to be able to search through existing recipes|
|                                       |3B| As a logged-in user, I want to be able to make my own collection of recipes which I can come back to|
|                                       |3C| As a logged-in user, I want to be able to make my cookbooks Public or Private|
|**SHARING**                            |  ||
|                                       |4A| As a logged-in user, I want to be able to share a recipe with a friend easily|
|                                       |4B| As a logged-in user, I want to be able to share just the ingredients to a friend easily|
|**USER PROFILE**                       |  ||
|                                       |5A| As a logged-in user, I want to view a list of my cookbooks|
|                                       |5B| As a logged-in user, I want to be able to edit my cookbooks|
|                                       |5C| As a logged-in user, I want to be able to add new recipes|
|                                       |5D| As a logged-in user, I want to be able to create my own variations of existing recipes|
|                                       |5E| As a logged-in user, I want to write a short bio about myself on my profile|
|**REVIEWS**                            |  ||
|                                       |6A| As a logged-in user, I want to leave a review on public recipes|
|                                       |6B| As a logged-in user, I want to be able to delete reviews on my own recipes|
|**CONTACT**                            |  ||
|                                       |7A| As a user, I want to see the websites contact details to raise an issue|

**Project Goal:**<br>
Create a website for collecting and sharing recipes which is useful, enjoyable and attractive for the largest range of users.

**Project Objectives:**<br> 
* To create a website with a simple and intuitive User Experience;
* To add content which is relevant and informative;
* To differentiate between user accounts and an admin account for non-code literate business content management;
* To implement fully functional features that will ease logged-in user's experience with the site and help them to integrate it's use into their lifestyle;
* To make the website available and functional on every device.<br><br>

### Scope<hr>
**Simple and intuitive User Experience**<br>
* Ensure the navigation menu is visible and functional at any stage of using the site;
* Ensure every page has a relevant name which fits its content;
* Ensure the users will get visual feedback when navigating through pages;
* Ensure the users will get visual feedback when navigating through recipes collections;
* Create a design which does not confuse users and matches a singluar brand image.

**Relevant content**<br>
* Recipes have clear instrustions, ingredients and descriptions;
* Menu and cookbook navigations blocks are clear and well designed;
* Create a scrollable page which shows all the recipes in the database;
* Create a section beneath each recipe with customer reviews for full transparency.

**Features for upgraded experience**<br>
* Create a favouriting system for prioritizing specific recipes in a cookbook;
* Create a business profile option for professional chefs to sell their cookbooks on the platform;
* Create a search function which includes food genres to allow groupings and style searches;
* Create a link with existing cupboard contents tracking apps so that ingredients needed lists can be generated with an awareness of what is already in the user's kitchen;
* The ability for future users to add whole cookbooks from other users collections.

**Different client and admin Accounts**<br>
* Admin accounts are able to block accounts for abusing the platform;
* Admin accounts can delete database entries which do not meet basic format compliances;
* Client accounts can create their own recipes, manage their own collections and create variant copies of other user recipes. They can also write reviews on any public recipes.

**Responsiveness**<br>
* Create a responsive design for desktop, tablet and mobile devices.<br><br>

### Structure<hr>
The structure of the website is divided into six pages; with content depending on account specifications <br>
-The **Home** page is visible for new and returning users, it includes an about section and buttons to register or login;<br>
-**Register/Login** is a pop-up overlay on top of the Home page;<br>
-**Logout** feature is a modal that helps user exit their current account;<br>
-The **Nav Menu** is the same across all pages however it is simplified before logging in;<br>
-The **Kitchen** page is only visible for the logged-in clients and displays the logged-in users collection of Cookbooks and Dishes along with a brief bio of the user;<br>
-The **Dish Wall** is the main display and acts as the home page for logged in users. It displays a scrollable gallery of Dish-Tiles from the database;<br>
-The **Create** page has two sub-pages, Create-Cookbook and Create-Dish;<br>
-The **Create-Cookbook** page allows users to name their book, rite a brief description and pic a cover;<br>
-The **Create-Dish** page allows users to create a recipe or Dish-Tile to add to the database;<br>
-**Contact Us** contains information visible to any users, even without registering;<br>
-The **Dish Tile** pages contain a recipe and display all it's details and reviews;<br>
_**Manage Features** allow an admin user to edit content generated by standard users.<br>

### Skeleton<hr>
**Wireframes**<br>
The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool and can be viewed [here](static/images/Wireframes.png)<br>

**Database**<br>
The project uses the PostgreSQL relational database for storing the data.<br>
Two diagrams were made to represent the relation between the tables

## Agile Methodology
This project was developed using the Agile methodology. User stories were central in planning steps taken. User stories were broken down into acceptance criteria and these were checked off using githubs project KanBan board functionality. These can all be seen publicly attached to this repo. Some acceptance criteria were beyond the scope of the educational project and timeline so have not been met. However they were retained to make it clear the greater goal for the project and to give context to what has already been built; compromises have been made where possible so that absolutely no core functionality for this first iteration and base version of the design have been left out.<br> 

## Features
### Existing Features<hr>
#### Create, Read, Update, Delete
Creation of dishes is a simple form, these can be read on the users profile or in the main dish wall on the home page and in the detailed iew of the recipe. Updating or editing this content is simple with the instance filled form accessible from the recipe details page for the authenitcated user who created the recipe, and the same is true of the delete function for these users. 

Creating cookbooks is again a simple form accessible in the user profile, populating them is then done on the recipes cards or on the homepage, reading them on the profile page and then the cookbook-contents page is straightforward for the authenticated user who created the cookbook (for the moment the collections cannot be seen by other users - however the draft function is already in place). Updating the contents of the cookbook is possible from the cookbook contents page where recipes can be removed, and the name, description and cover image can be changed. Deletion of the cookbooks is done from the user profile. 

Comments can be added, read, edited and deleted by the user's that create them. They must be authorised by admin for other users to read them. 

#### Chef Profiles
The users' accounts have been created using the **django allauth** module. This way, information about the current user can be accessed from the template and displayed for the user to access the site. The chef profile model contains a bio, a profile picture, a location, birth date and socials links fields. These are displayed on the user's profile (other than the birthdate which remains private and is redundant at this stage but could be used in future for profile recovery or age restricted content). The profile can be edited easily and is accessed on the view_chefprofile page along with all the user's other content, such as their recipe's and cookbooks, for easy access and management.<br>

### Testing
## Manual Testing
Each user experience function was tested thoroughly by manually logging in as a non-admin user and attempting to take the steps to create content, read content, edit content and delete content. This is true for reviews, recipes and cookbooks as well as user profiles. 

The defensive programming has also been tested manually. By finding the url of a particular post, then logging out, and attempting to access this same url. The @login_required decorator on the views for post_details stops unauthorised users from accessing anything other than the index, which only shows a welcome and prompt for registering and the about and contact pages. The @login_required addition to settings allows us to set a specified redirect for any unauthorised attempt to any accepted url and view which uses this decorator. My setting simply returns the attempt to the index. 

The admin functionalities, for creating, editing, deleting, authorizing and managing all models in the database has been thoroughly tested in the making of the site. 

All the forms used in the site have been thoroughly tested for non-valid attempts and valid attempts with unusual entries. The slug generator in particular caused some unfortunate bugs when spaces and non-alphanumeric characters were used which had to be handled in the views.py file with several methods to remove any non-alpha characters and spaces as well as adding a distinct number to each newly generated string. This was all thanks to manual testing. 

Image uploads have all been tested for large and small images with long and shortside differences, these are managed effectively to give a consistent layout on all pages after upload. 

## Django Testing

All forms in the chef profile app were tested using automatic django tests.py files to test for validity. 
The comments were tested for validity. 
The views.py for the posts detail was tested for functionality also. 

## Validator Testing 
[JsHint](https://jshint.com/) - used for validating the javascript code<br>
[PEP8 Validator](http://pep8online.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
[W.A.V.E.](https://wave.webaim.org/) - for testing accessibility<br>
[LightHouse] - for testing performance<br>


## Unfixed Bugs

There are no unfixed bugs that I am aware of at this time. My aim was to have everything which is included working smoothly before submission, rather than adding lots of extra features which were not properly tested or unfinished and beyond the requirements of the prokect scope. 

## Responsive Layout and Design
The project design has been adapted to all types of devices using Bootstrap predefined breakpoints and Chrome's DevTools to digitally test the platform across a number of devices. Three specific media queries were added to solve minor layout issues at specific breakpoints.

**Tested devices:**

    - iPhone SE 
    - iPhone XR 
    - iPhone 12 Pro
    - iPhone 14 Pro Max
    - Pixel 7
    - Samsung Galaxy S8+ 
    - Samsung Galaxy S20 Ultra
    - Ipad Mini
    - Ipad Air 
    - Ipad Pro 
    - Surface Pro 7
    - Surface Pro Duo 
    - Galaxy Fold
    - Samsung Galaxy A51/71 
    - Nest Hub
    - Nest Hub Max

## Tools Used

[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[CodeAnywhere](https://app.codeanywhere.com/) - Used as an IDE for the first half of the project before their system seemed to crash for several days<br>
[GitPod](https://gitpod.io/workspaces) - Used as an IDE for the remained of the project, fantastic tool<br>
[Visual Studio](https://code.visualstudio.com/) - for holding code snippets while new method were tested<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project<br>
[Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[Font Awesome](https://fontawesome.com/) - used for the icons<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predifined styled elements and creating responsiveness<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[JsHint](https://jshint.com/) - used for validating the javascript code<br>
[PEP8 Validator](http://pep8online.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
[Chrome Del Tools](https://developer.chrome.com/docs/devtools/) - for debugging the project<br>
[W.A.V.E.](https://wave.webaim.org/) - for testing accessibility<br>
[Cloudinary](https://cloudinary.com/) - for storing static data<br>
[LightHouse] - for testing performance<br>

### Python packages

* asgiref==3.7.2
* cloudinary==1.36.0
* crispy-bootstrap5==0.7
* dj-database-url==0.5.0
* dj3-cloudinary-storage==0.0.6
* Django==4.2.10
* django-allauth==0.57.2
* django-cloudinary-storage==0.3.0
* django-crispy-forms==2.1
* django-formtools==2.5.1
* django-summernote==0.8.20.0
* gunicorn==20.1.0
* oauthlib==3.2.2
* psycopg2==2.9.9
* PyJWT==2.8.0
* python3-openid==3.2.0
* requests-oauthlib==1.3.1
* sqlparse==0.4.4
* urllib3==1.26.18
* whitenoise==5.3.0

## Deployment

### Deploy on Heroku
 1. Create Pipfile 
 
 In the terminal enter the command ` pip3 freeze > requirements.txt`, and a file with all requirements will be created. 
 
 2. Setting up Heroku

    * Go to the Heroku website (https://www.heroku.com/) 
    * Login to Heroku and choose *Create App* 
    * Click *New* and *Create a new app*
    * Choose a name and select your location
    * Go to the *Resources* tab 
    * From the Resources list select *Heroku Postgres*
    * Navigate to the *Deploy* tab
    * Click on *Connect to Github* and search for your repository
    * Navigate to the *Settings* tab
    * Reveal Config Vars and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.    

3. Deployment on Heroku

    * Go to the Deploy tab.
    * Choose the main branch for deploying and enable automatic deployment 
    * Select manual deploy for building the App 
    
The live link can be found here - https://menooh-49c095ee8d82.herokuapp.com/

<hr>

## Credits
### Content
* The content of the website is taken from several recipe websites, this site is for educational purposes only so no rights have been challenged. OpenAI's ChatGPT was kind enough to produce the content for my fixtures file so that it wasn't just an empty site with cheese on toast recipes designed by myself. 
### Media
* All images have been harvested from google image searches of the dishes names, I reiterate this site is for educational purposes only and no images or recipes shown connected to images are sold or are for profit. No images with a watermark were selected or tampered with. 
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
### Code
* The method for applying infinite scroll came from [here](https://simpleisbetterthancomplex.com/tutorial/2017/03/13/how-to-create-infinite-scroll-with-django.html)
* The initial approach for the dish wall layout came from [here](https://github.com/sobriquette/pinclone/tree/master)
* The core of the method for using index counters in a For Loop to give the varied sizes came from [here](https://copyprogramming.com/howto/python-index-counter-in-django-template-forloop)
* The lesson on how to shorten long titles and excerpts to "..." [here](https://stackoverflow.com/questions/29925447/how-to-display-at-the-end-of-a-very-long-title-bootstrap)
* Some of the early building blocks of the site and a helpful guide was [here](https://www.freecodecamp.org/news/how-to-create-a-portfolio-website-using-html-css-javascript-and-bootstrap/)
* After issues with the infinite scroll this was very helpful [here](https://refine.dev/blog/what-is-htmx/#installing-htmx)

## Acknowledgements
- Code Institute for the knowledge and all the tutor support. In particular Joanne, thank you!<br>
- Bruno at CodeAnywhere who got me through some dark days when my workspace wouldn't play ball.<br>
<hr>