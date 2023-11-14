# Menooh - Cookbook Building Website
<img src="static/media/responsive.png" ><br>
<hr>

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
    - [Fork the repository](#fork-the-repository)
    - [Clone the repository](#clone-the-repository)
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
* To add conent which is relevant and informative;
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
* Create a business profile option for professional chefs to sell their cookbooks on the plaform;
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

* FLOWCHARTS
The Flowchart for my program was created using <b>LucidChart</b> and it visually represents how the system works.<br>
[![N|Solid](static/media/flowchart.png)](static/media/flowchart.png)<br><br>


### Skeleton<hr>
**Wireframes**<br>
The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool and can be viewed [here](static/wireframes/wireframes.pdf)<br>

**Database**<br>
The project uses the PostgreSQL relational database for storing the data.<br>
Two diagrams were made to represent the relation between the tables, the initial one and the final one.
The first one was created before the actual development of the website which led to some changes to the attributes and tables for finding the most relevant and useful ones to be kept.

<details>
  <summary>Initial Schema</summary>
<img src="static/media/initial_db.jpeg" ><br>
</details>

<details>
  <summary>Final Schema</summary>
<img src="static/media/final_db.jpeg"><br>
</details><br>

### Surface<hr>
#### Color Scheme
All the colours were selected with the eyedropper plugin from the website cover, to maintain chromatic harmony. <br>
* The primary colour scheme was used for most of the text existent on the website, in either dark or bright colours for creating a good contrast.<br> 
<img src="static/media/clr2.png" width="30%">
<img src="static/media/clr3.png" width="30%">
<img src="static/media/clr4.png" width="30%">
<img src="static/media/clr1.png" width="30%"><br>

* The secondary colour scheme was used for buttons, warnings, errors or for highlighting important information.<br>
<img src="static/media/clr5.png" width="30%">
<img src="static/media/clr6.png" width="30%">
<img src="static/media/clr7.png" width="30%">
<img src="static/media/clr8.png" width="30%">

#### Fonts
* The fonts I used for this site were imported from [Google Fonts](https://fonts.google.com/):<br>
**Body:** *Tiro Devanagari Marathi, serif*<br>
**Navbar:** *Courgette, cursive*<br>
**Logo:** *Cinzel, serif*<br>
**Slogan:** *Marck Script, cursive*<br>

#### Visual Effects
* **Box shadows** <br>
Multiple box shadows were used for the cover, buttons and images. They were inspired from [css-box-shadow-examples]("https://getcssscan.com/css-box-shadow-examples")<br>
* **Animation**<br>
Some animations were used for creating a dynamic and attractive design
<details>
  <summary>View Moving arrows animation</summary>
<img src="static/media/arrows-capture.gif"><br>
</details>
<details>
  <summary>View Authentication links Pulse animation</summary>
<img src="static/media/pulse-capture.gif"><br>
</details>

* **Hover effects**<br>
<details>
  <summary>View NavBar elements hover</summary>
<img src="static/media/nav-capture.gif"><br>
</details>
<details>
  <summary>View Buttons hover</summary>
<img src="static/media/delete-capture.gif"><br>
</details>
<details>
<summary>View Footer elements hover</summary>
<img src="static/media/footer-capture.gif"><br>
</details><br>

## Agile Methodology
This project was developed using the Agile methodology.<br>
All epics and user stories implementation progress was registered using [Trello](https://trello.com/). As the user stories were accomplished, they were moved in the Trello board from **To Do**, to **In-Design**, **Testing** and **Done** lists. 
<details>
<summary>Sprints Details</summary>

* **Sprint 1 - SETUP**<br>
    -Setup Django<br>
    -Deploy on heroku<br><br>
* **Sprint 2 - CONTENT AND NAVIGATION**<br>
    -Create a navigation menu<br>
    -Add restaurant name, slogan and description<br>
    -Choose colors, fonts and decorative images <br><br>
    <img src="static/media/sprint2.png"><br><br>
* **Sprint 3 - USER REGISTRATION/AUTENTHICATION**<br>
    -Implement the *Register* page using the django-allauth module<br>
    -Implement the *Login* page using django-allauth module<br>
    -Implement *Logout* modal using django-allauth module<br><br>
    <img src="static/media/sprint3.png"><br><br>
* **Sprint 4 - BOOKING**<br>
    -Create *Booking* page<br>
    -Implement a feature to display available tables<br>
    -Implement booking form validation<br><br>
    <img src="static/media/sprint4.png"><br><br>
* **Sprint 5 - USER PROFILE**<br>
    -Create user *Profile* page<br>
    -Implement *Upcoming bookings* section<br><br>
    <img src="static/media/sprint5.png"><br><br>
* **Sprint 6 - STAFF MANAGE BOOKINGS**<br>
    -Create a *Manage Bookings* page to display all bookings for today<br>
    -Implement filtering by date form<br><br>
    <img src="static/media/sprint6.png"><br><br>
* **Sprint 7 - REVIEWS**<br>
    -Create a *Reviews* page to display all reviews<br>
    -Implement form for adding and updating review<br>
    -Complete *Home* page and add *Top Reviews* section<br><br>
    <img src="static/media/sprint7.png"><br><br>
* **Sprint 8 - MENU**<br>
    -Create a *Menu* page to display menu details<br>
    -Implement a feature for adding meals to favourites<br>
    -Complete the *Profile* page and add the *Favourite dishes* section<br>
    -Complete *Home* page and add *Most appreciated dishes* section<br><br>
    <img src="static/media/sprint8.png"><br><br>
* **Sprint 9 - CONTACT**<br>
    -Create *Where to find us* page<br>
    -Add timetable<br>
    -Add location address and map<br>
    -Add contact details<br><br>
    <img src="static/media/sprint9.png"><br><br>
* **Sprint 10 - TESTING**<br>
    -Create unit tests for Home App<br>
    -Create unit tests for Booking App<br>
    -Create unit tests for Menu App<br>
    -Create unit tests for Reviews App<br>
    -Create unit tests for Contact App<br>
</details><br><br>

## Features
### Existing Features<hr>
#### Create bookings
Every user that is authenticated can access the *Bookings* page for making a reservation. This feature provides a form with multiple sections that appear successively, as steps in completing the booking.
* The first section is for selecting the date and time interval of the booking<br>
    The inputs are validated after the following rules:
    * The Date value should not be less than the current day;<br>
    * For the current day the Start hour can't be less than the current hour;<br>
    * End Hour should be greater than Start hour;<br>
    * Start and End hours must be between 9:00 AM - 11:00;<br><br>
<img src="static/media/booking1.png" width="60%"><br><br>

* The next section appears only if the previous one is valid and it displays the tables existing in the restaurant in the colour that matches their availability status. The user can now choose a table from the dropdown, considering that it only contains the free tables. Also, there is a read-only input with a value that represents the number of seats for each selected table, as an informative element.<br> 
<img src="static/media/booking2.png" width="40%"><br><br>

* Another part of the form is displayed with the contact details to be filled in. A better alternative available for the users that are not staff members is to check the *Book it on my name* option. This means that the form will automatically register the authenticated user's name and email as contact details.<br>
<img src="static/media/booking3.png" width="40%"><br><br>

* The last section contains an overview of the booking. If the reservation is submitted, a success message will appear
<img src="static/media/booking4.png" width="60%"><br><br>
<img src="static/media/booking5.png" width="40%"><br><br>

#### Reviews
* On the *Reviews page* there is a list of all the reviews posted on the website and it is visible to all types of users. All the reviews have the same design and type of content. Important details are displayed such as *Name*, *Date and time*, *Stars rating* and the *Message* posted.<br>
<img src="static/media/reviews1.png" width="60%"><br><br>

* When a user is authenticated and he never posted a review, a form is provided for leaving a message and a star rating.<br>
<img src="static/media/reviews2.png" width="40%"><br><br>

* For authenticated users that already posted a review, the page displays the values of their review and the possibility to update it.<br>
The form for editing the review already contains the corresponding message value and the star ratings in the initial state.<br>
<img src="static/media/reviews3.png" width="40%"><br><br>
<img src="static/media/reviews4.png" width="40%"><br><br>


#### Menu 
* On the *Menu* page there is a list with all the menu elements. Every item represents a meal with details such as *Name*, *Image*, *Price*, and Ingredients. The list design is simple and attractive.<br>
<img src="static/media/menu1.png" width="70%"><br><br>

* An interactive feature has been added that is only available for logged-in users that are not staff members. A user has the possibility to mark his favourite meals through a form that uses a heart icon as a button. The heart shape defines the state of the meal, which can be marked or unmarked as a favourite dish.<br>
<img src="static/media/menu2.png" width="30%">
<img src="static/media/menu3.png" width="30%"><br><br>

#### Profiles
The users' accounts have been created using the **django allauth** module. This way, information about the current user can be accessed from the template and displayed for confirming that the authentication was successful.<br>
Considering that the website is created for a restaurant, the profile of the user is created to display essential information such as name and email.<br>
<img src="static/media/profile1.png"><br><br>
Also, the profile page contains two features that are created for giving the user a better experience with the website.<br><br>
* One of the features is called **Your upcoming bookings** and is represented by a list of the bookings created by the currently authenticated user.<br>
Every booking has a visual representation of a note with the details of the reservation written on it. <br>
<img src="static/media/profile2.png"><br><br>
Also, for giving the user the ability to manage his bookings, every element in the list comes with a *Delete Booking* button.<br>
The button triggers a modal for confirmation, that being a part of the defensive programming.<br>
<img src="static/media/profile3.png"><br><br>

* Another user-friendly feature is **Your favourite dishes**. This feature displays to the user all the meals that he has added to *Favourites* from the *Menu* page. The menu items contain the meal image and name, as it was not considered necessary to display all the details from the menu.<br>
<img src="static/media/profile4.png"><br><br>

#### Staff bookings management
The staff account was created as a superuser account from the terminal and also has access to the admin panel.<br>
There is a page created especially for staff members to keep a better tracking of all the reservations that are being made for the restaurant.<br>
* The bookings are displayed on a custom-designed table, grouped by day and ordered by time. The page renders by default the reservations for the current day and their number.<br>
* A form is provided for filtering the bookings by date for a better user experience.<br>
* A booking also has a delete button that triggers a confirmation modal. <br>

<img src="static/media/staff1.png" width="80%"><br><br>
<img src="static/media/staff2.png" width="50%"><br><br>

* If the bookings list is empty, a suggestive message is displayed.<br>
<img src="static/media/staff3.png" width="50%"><br><br>


### Future Feature Considerations<hr>
* Updating the booking feature with a more complex algorithm and design for generating the available tables. The current algorithm sets a table as *busy* even if it is registered as booked only for a small part of the interval requested by the user for the reservation. Also, the Start and End time are restricted to accept only zero hundred hours. By changing the limit to even zero-thirty hours, the tables algorithm will be more efficient.

* Another possible feature would be the implementation of a *Reward system*. Every time a client leaves a good review, a discount would appear on his profile page to use on his next visit. Also, a user should be given the status of *Loyal customer* when he registers on a system every time he eats, if that happens regularly. Different discounts should apply to loyal customers in order to recompensate and encourage their habit.  

## Responsive Layout and Design
The project design has been adapted to all types of devices using Bootstrap predefined breakpoints. For intermediate devices where the design didn't fit accordingly, custom breakpoints were used.

**Breakpoints:**

    - max-width:280px
    - max-width:768px
    - max-width:992px
    - max-width:1024px

**Tested devices:**

    - Moto G4 
    - iPhone SE 
    - iPhone XR 
    - iPhone 11 
    - iPhone 13
    - iPhone 5/SE 
    - iPhone 6/7/8 
    - Ipad
    - Ipad Air 
    - Ipad Mini
    - Ipad Pro 
    - Pixel 5 
    - Surface Duo 
    - Surface Pro 7 
    - Nest Hub 
    - Nest Hub Max
    - Samsung Galaxy S20 Ultra 
    - Samsung Galaxy S8 
    - Galaxy Note 2 
    - Galaxy Tab S4
    - Asus Vivobook

## Tools Used

[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[Visual Studio](https://code.visualstudio.com/) - for writing and testing the code<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project<br>
[TablePlus](https://tableplus.com/) - for managing the database entries<br>
[Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes<br>
[LucidChart](https://www.lucidchart.com/) - used for creating the Flowchart and Database relational schema<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[Diffchecker](https://www.diffchecker.com/) - used for comparing the code<br>
[TinyPNG](https://tinypng.com/) - for compressing the images<br>
[Grammarly](https://app.grammarly.com/) - for correcting text content<br>
[Font Awesome](https://fontawesome.com/) - for creating atractive UX with icons<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predifined styled elements and creating responsiveness<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[JsHint](https://jshint.com/) - used for validating the javascript code<br>
[PEP8 Validator](http://pep8online.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
[Chrome Del Tools](https://developer.chrome.com/docs/devtools/) - for debugging the project<br>
[W.A.V.E.](https://wave.webaim.org/) - for testing accessibility<br>
[Cloudinary](https://cloudinary.com/) - for storing static data<br>
LightHouse - for testing performance<br>

### Python packages

* django 
* gunicorn 
* dj-database-url
* psycopg2
* dj3-cloudinary-storage 
* pylint-django 
* whitenoise
* jinja2 
* django-allauth
* django-crispy-forms 
* django-braces 
* django-filter
* django-annoying 
* coverage
* pylint 
* python-dotenv 
* dateutils 
* autopep8

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
    
### Fork the repository
For creating a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:
- On [My Repository Page](https://github.com/useriasminna/website-booking-website), press <i>Fork</i> in the top right of the page
- A forked version of my project will appear in your repository<br></br>

### Clone the repository
For creating a clone of the repository on your local machine, use<b>Clone</b>:
- On [My Repository Page](https://github.com/useriasminna/website-booking-website), click the <i>Code</i> green button, right above the code window
- Chose from <i>HTTPS, SSH and GitClub CLI</i> format and copy (preferably <i>HTTPS</i>)
- In your <i>IDE</i> open <i>Git Bash</i>
- Enter the command <code>git clone</code> followed by the copied URL
- Your clone was created
<hr>

## Credits
### Content
* The content of the website is fictive. 
### Media
* All .png images used on the site were taken from [pngegg](https://www.pngegg.com/)
### Code
* The code for creating a custom user model was taken and adapted from [here](https://www.codingforentrepreneurs.com/blog/
how-to-create-a-custom-django-user-model/)
* The validation for the booking form was inspired from [here](https://www.javascripttutorial.net/javascript-dom/javascript-form-validation/)
* The method of inserting data into HTML for javascript was inspired from [here](https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/)
* Django pagination was taken and adapted from [here](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html)
* Pagination with a query set was inspired from [stackoverflow](https://stackoverflow.com/questions/68155106/filter-class-based-view-listview-that-has-pagination)
* Custom arrows for input type number were taken and adapted from [stackoverflow](https://stackoverflow.com/questions/63544101/customize-increment-arrows-on-input-of-type-number-using-css)

## Acknowledgements
- Code Institute for all the material and support offered<br>
- My mentor Ben Kavanagh for great tips and his willingness to help me as much as possible with the problems encountered during the development of the project<br>
- Slack community for great involvement in helping each other<br>
<hr>