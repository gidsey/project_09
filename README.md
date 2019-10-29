# Treehouse Python Techdegree: Project 09

## Improve a Django Project

Refractor and improve efficency of an existing Django project.

## Changes made to Models:

#### Menu
default added to 'expiration_date' field to prevent None type results.

'expiration_date' changed from `DateTimeField` to `DateField`

#### Item
`on_delete=models.CASCADE` added to 'chef' foriegn key field 

##### Ingredient
add `unique=True` to name


## Atributions

Icons: soda by Ben Davis from the [Noun Project](https://thenounproject.com)

Project work by [Chris Guy](https://www.linkedin.com/in/gidsey/), October 2019


