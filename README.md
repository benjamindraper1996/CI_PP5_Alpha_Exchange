# Alpha-Exchange
(Developer: Benjamin Draper)

![Mock-up image](documentation/wireframes/am-i-responsive.jpg)

 [Live webpage]()

## About
Alpha Exchange is an E-commerce website aimed at B2C sales with a drop shipping style model, this website mainly features clothing, home-wear and accessories. the website is designed to allow users to experience a fully featured shopping experience where you can easily find known products, search for new or similar products, filter by categories or browse through the new arrivals and clearance sections.

### User Information
user information

### Card Information
- Test Card Number: 4242 4242 4242 4242 
- Expiration Date: Any future date (e.g. 02/24) 
- CVC: Any three digits (e.g. 424)

## Table of Content
1. [Project Goals](#project-goals)
    1. [Website User Goals](#website-user-goals)s
    2. [Website Owner Goals](#website-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [Business Model](#business-model)
    4. [SEO](#seo)
    5. [Marketing](#marketing)
3. [User Stories](#user-stories)
4. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colour](#colour)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Database](#database)
    6. [Wireframes](#wireframes)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
    3. [Libraries](#libraries)
6. [Features](#features)
7. [Validation](#validation)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [JavaScript Validation](#javascript-validation)
    4. [Python Validation](#python-validation)
    5. [Accessibility](#accessibility)
    6. [Performance](#performance)
    7. [Device Testing](#device-testing)
    8. [Browser Compatibility](#browser-compatibility)
8. [Testing user stories](#testing-user-stories)
9. [Bugs](#bugs)
10. [Deployment](#deployment)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

## Project Goals
### Website User Goals
- As a website user, I want to be able to have easy options to navigate around the website.
- As a website user, I want to be able to view the products available on the website.
- As a website user, I want to be able to apply filters to the products.
- As a website user, I want to be able to search for specific products.
- As a website user, I want to be able to contact the site owner if I have any questions.
- As a website user, I want to be able to add items to a basket and checkout my order.
- As a website user, I want to be able to register for an account.
- As a website user, I want to be able to log in and out of my existing account.
- As a website user, I want to be able to review past orders I have made from my account.
- As a website user, I want to be able to sign up to a newsletter.
- As a website user, I want to be able to view and edit my profile.

### Website Owner Goals
- As the website owner, I want to allow users to navigate the website with ease.
- As the website owner, I want to allow users to view the product details.
- As the website owner, I want to allow users to be able to add items to the basket and purchase items.
- As the website owner, I want to allow users to create an account.
- As the website owner, I want to allow users to sign in and out when they return to the website.
- As the website owner, I want to promote the website to new and existing users.
- As the website owner, I want to allow users to see their order history.
- As the website owner, I want to allow users to sign up for a news letter.
- As the website owner, I want to be able to add, edit and delete items from the website myself.

[Back to Table Of Content](#table-of-content)

## User Experience
### Target Audience
- This website is targets people are looking to buy clothing.
- This website is targets people are looking to buy accessories.
- This website is targets people are looking to buy gifts for friends and family.
- This website is targets people are looking to sign up to the newsletter.
- This website is targets people are looking to discover what we currently have to offer.

### User Requirements and Expectations
- The user can expect an intuitive and accessible navigation system.
- The user can expect to easily find the products available.
- The user can expect to easily find specific products they are looking for through filtering and the search function.
- The user can expect all links work as expected and functions perform their tasks correctly.
- The user can expect presentation is in line with the website guidelines and the website is visually appealing on all screen sizes.
- The user can expect easy to read headings to tell the users at a glance what they are looking at.
- The user can expect accessibility features to be clearly defined.
- The user can expect to be able to complete any purchase made and track previous orders through their account.
- The user can expect to be able to contact the business for further queries.

### Business Model
This website is primarily aimed at selling to consumers, for this I have chosen a B2C business model. To make the website more consumer friendly I have made sure that all design decisions, pictures, navigation and ease of purchase is made with the end user in mind.
The business model would be that this website is able to be used as a dropshipping website where the website owner does not need to handle inventory and the products can be sent straight from the supplier.
As an alternative the website owner could buy the product and arrange the shipping of orders themselves, this does mean any returns also get handled by the website owner.
For This project I have chosen for the stock to be handled by a third party.

### SEO
Long tag keywords and short tag keywords were searched for in regards to SEO using Google tools and other online resources. These tags are included within the main HTML head and in the appropriate places within the project to name images and within main body text.

![SEO keywords HTML]()

### Marketing
#### Facebook Page
To help market the website, the website includes a like to its own social media page in the footer where new products and announcements are made.
the Facebook page can be viewed [here](). 

![Facebook Screenshot]()

#### Newsletter Sign up
The website includes a sign up form to a newsletter so the business can keep in touch with anyone who want more information.

![Sign-up]()

![Email-success]()

[Back to Table Of Content](#table-of-content)

## User Stories
### Unauthenticated Users
1. As a unauthenticated user, I would like to be able to navigate through the website easily so that it is easy to find the information I am looking for.
2. As a unauthenticated user, I would like to be able to sign up for an account so that I can view my profile and track my orders.
3. As a unauthenticated user, I would like to see the available products that are listed on the website so that I can see what is currently in available.
4. As a unauthenticated user, I would like to know how to find social media links so that I can find out about new products and news.
5. As a unauthenticated user, I would like to be able to search or filter the website for specific products and brands so that I can find exactly what i am looking.
6. As a unauthenticated user, I would like to be able to sort and view products by category so that I can find specific products easily.
7. As a unauthenticated user, I would like to be able to order the products on a page a variety of ways so that I can find what I am looking for easier.
8. As a unauthenticated user, I would like to be able to see detailed description of the products available so that i can make an informed purchase.
9. As a unauthenticated user, I would like to be able to add a product to my basket so that I can purchase them.
10. As a unauthenticated user, I would like to be able to see the products that are in my basket so that I don't spend too much.
11. As a unauthenticated user, I would like to be able to increase quantities and remove items from my basket so that I don't have to navigate to the store and add the item again each time.
12. As a unauthenticated user, I would like to be able to purchase the items in my basket so that I can complete my order.
13. As a unauthenticated user, I would like to be able to log in to / sign out of an existing account so that I can get updated on my orders.
14. As a unauthenticated user, I would like to be able contact the business so that I can ask any questions.
15. As a unauthenticated user, I would like to be able to sign up to the newsletter so that I can receive news and updates from the business.
### Authenticated Users
16. As a authenticated user, I would like to be able to view and update my personal information so that I do not have to fill it out each time I make an order.
17. As a authenticated user, I would like to be able to view my order history so that i can find products i have ordered before and would order again.
### Website Staff
18. As a website staff user, I would like to be able to use full CRUD functionality so that I can update the product range available.
19. As a website staff user, I would like to be able to manage product inventory so that I can adjust the available products.
20. As a website staff user, I would like to be able to view and update product categories so that the product range is up to date.
21. As a website staff user, I would like to be able to add product categories so that new products are available on the website.
22. As a website staff user, I would like to be able to delete product categories so that products that are no longer available are removed.