# Menooh - Cookbook Building Website
<img src="static/media/responsive.png" ><br>
<hr>

The live link can be found here - https://menooh-49c095ee8d82.herokuapp.com/

## Table of contents
- [Menooh - Cookbook Building Website](#menooh---cookbook-building-website)
  - [Table of contents](#table-of-contents)
  - [Overview](#overview)
  - [UX](#ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
      - [Color Scheme](#color-scheme)
      - [Fonts](#fonts)
      - [Visual Effects](#visual-effects)
  - [Agile Methodology](#agile-methodology)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Create bookings](#create-bookings)
      - [Reviews](#reviews)
      - [Menu](#menu)
      - [Profiles](#profiles)
      - [Staff bookings management](#staff-bookings-management)
    - [Future Feature Considerations](#future-feature-considerations)
  - [Responsive Layout and Design](#responsive-layout-and-design)
  - [Tools Used](#tools-used)
    - [Python packages](#python-packages)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Deploy on Heroku](#deploy-on-heroku)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
  - [Acknowledgements](#acknowledgements)

## Overview
This project is designed and developed to help users create and manage their own recipe books for cooking at home. Think Pinterest for foodies. The users are given the option to create their own recipes, add recipes from other users cookbooks, and create variants of other users recipes. Users can then forward a single recipe to a contact for the purposes of preparing that meal and purchasing ingredients. All these functionalities are available to any user with an account. <br>
The website was created for domestic users, but there is no reason that businesses wouldnt also use it. This is a working demonstration of this site model which has the potential to be scaled to a functioning business in it's own right. <br>
**Menooh - cookbook building website** was developed using Python (Django), HTML, CSS and JavaScript by storing the data in a PostgreSQL database.
<br><br>
The fully deployed project can be accessed at [this link](https://menooh-culinary-website.herokuapp.com/).<br><br>

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
-The **Explore** page lets users search for grouped sets of Dish Tiles;<br>
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

<details>
  <summary>Initial Schema</summary>
<img src="static/media/initial_db.jpeg" ><br>
</details>

<details>
  <summary>Final Schema</summary>
<img src="static/media/final_db.jpeg"><br>
</details><br>


#### Fonts
* The fonts I used for this site were imported from [Google Fonts](https://fonts.google.com/):<br>
**Body:** *Tiro Devanagari Marathi, serif*<br>
**Navbar:** *Courgette, cursive*<br>
**Logo:** *Cinzel, serif*<br>
**Slogan:** *Marck Script, cursive*<br>


## Agile Methodology
This project was developed using the Agile methodology.<br>
All epics and user stories implementation progress was registered using [Trello](https://trello.com/). As the user stories were accomplished, they were moved in the Trello board from 


## Features
### Existing Features<hr>
#### Create 

* Th<br> 
<img src="static/media/booking2.png" width="40%"><br><br>

#### Reviews

#### Profiles
The users' accounts have been created using the **django allauth** module. This way, information about the current user can be accessed from the template and displayed for confirming that the authentication was successful.<br>

### Future Feature Considerations<hr>
* Upda

## Responsive Layout and Design
The project design has been adapted to all types of devices using Bootstrap predefined breakpoints. For intermediate devices where the design didn't fit accordingly, custom breakpoints were used.

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

## Testing
The testing documentation can be found at [TESTING.MD](TESTING.MD)

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