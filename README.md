# Treehouse Python Techdegree: Project 09

## Improve a Django Project

Improve the efficiency of an existing Django project.

## Changes

#### Functional
* Project upgraded from Django 1.9.9 to 2.2.7
* Admin area customised
* Expiration date data type changed from `DateTime` to `Date`
* Ingredient field set to be `unique`
* Migrations added to convert existing data
* Database queries optimised
* Template inheritance added
* Basic form validation added
* Custom form validation added
  - Menu expiry date cannot be set in the past
  - Brand names not permitted in Season name
* Confirmation messages added
* Delete menu functionality added
* Users must be authenticated to access add menu, edit menu or delete menu pages

#### Display
* Site upgraded to Bootstrap 4
* Page styling improved
* Django widget_tweaks added to form for better user experience
* JavaScript datepicker added
* Favicon added

#### Testing
* Unit tests added for Models, Forms Views
* 95% coverage achieved
 
## Running Locally

```bash
git clone https://github.com/gidsey/project_09.git
```

```bash
pip install -r requirements.txt
```
  
```bash
 python manage.py migrate
```

```bash
 python manage.py runserver
```

## Atributions

Date Picker by [Fengyuan Chen](https://fengyuanchen.github.io/datepicker/) 

Icons: soda by Ben Davis from the [Noun Project](https://thenounproject.com)

Project work by [Chris Guy](https://www.linkedin.com/in/gidsey/), November 2019


