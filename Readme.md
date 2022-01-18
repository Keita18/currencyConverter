# Currency Converter
This application allows you to convert currency using Fixer.io Api.
You have up to 170 currencies available

## Commands
- from country: ``rates, for example USD, EUR, GBP...`` or to exit `-exit`
- to country: ``rates, for example CAD, RUB, CHF...``
- amount: ``integer value``

## API
https://fixer.io/

## Demonstration
![b](img/a.png)
![b](img/b.png)

## Docker
1) Download the project to yourself.
2) Run command: 
   - docker build -t currency-converter .
   - docker run -it temperature-converter


## Testing
* main 
* [![CI](https://github.com/Keita18/currencyConverter/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/Keita18/currencyConverter/actions/workflows/python-app.yml)

* dev 
[![CI](https://github.com/Keita18/currencyConverter/actions/workflows/python-app.yml/badge.svg?branch=dev)](https://github.com/Keita18/currencyConverter/actions/workflows/python-app.yml)
