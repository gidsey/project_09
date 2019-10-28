# Treehouse Python Techdegree: Project 09

## Improve a Django Project

Refractor and improve efficency of an existing Django project.

## Changes made to Models:

#### Menu
`null=True` removed from 'expiration_date' field
default added to 'expiration_date' field to prevent None type results.

#### Item
`on_delete=models.CASCADE` added to 'chef' foriegn key field 

##### Ingredient
add `unique=True` to name




