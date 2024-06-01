# Country Info SOAP API using Python

This project demonstrates how to interact with a SOAP API using Python and the `zeep` library. It uses the CountryInfoService WSDL to fetch various information such as a list of continents, country currency, and country flags.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [List of Operations](#list-of-operations)
  - [List of Continents](#list-of-continents)
  - [Country Currency and Flag](#country-currency-and-flag)
- [What is a SOAP API?](#what-is-a-soap-api)

## Introduction

This project uses the `zeep` library to interact with the CountryInfoService SOAP API which is a free soap api.
```bash
http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL
```

This WSDL file offers a nice big learning playground. Few of its several services include fetching the country’s capital, currency, flag (as jpeg image), phone code etc.
It includes functions to list available operations, fetch a list of continents, and retrieve information about a country's currency and flag.

## Installation

To run this project, you need to have Python installed. You also need to install the `zeep` library. You can install it using pip:

```bash
pip install zeep
```
##Usage
List of Operations
The ListOfOperations function lists all the available operations in the WSDL service. Use this function to explore what operations you can perform with the SOAP API.

```python
ListOfOperations()
```


List of Continents
The Continents function fetches and prints a list of continents available in the WSDL service. Use this function to retrieve the names and codes of all continents.
```python
Continents()
```

Country Currency and Flag
The getCountryCurrencyAndFlag function retrieves the currency and flag of a specified country. Pass the ISO country code as an argument to this function to get the desired information.

For example, to get the currency and flag of the United States, you would call:

```python
getCountryCurrencyAndFlag("US")
```

## What is a SOAP API?
SOAP (Simple Object Access Protocol) is a protocol used for exchanging structured information in the implementation of web services. It relies on XML for its message format and usually runs over HTTP or SMTP. SOAP APIs are known for their robustness and extensibility, making them suitable for enterprise-level applications where security, transactions, and ACID compliance are crucial.

## Why Use SOAP API?
Standardized Protocol: SOAP is a protocol, while REST is an architectural style. SOAP provides a standardized way to communicate with web services.
Extensibility: SOAP has built-in error handling and allows for extensions to the protocol.
Security: SOAP supports security features like WS-Security, making it a good choice for applications that require enhanced security.
ACID Compliance: SOAP can handle transactions and ensure ACID compliance, which is essential for many enterprise applications.
