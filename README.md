# PyPayant

PyPayant is a python wrapper for the invoicing platform [pypayant](http://payant.ng/)

It provides features available in the API:

* Clients
* Invoices
* Payments
* Products
* Miscellaneous

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Set Up
    Go to [pypayant](http://payant.ng/) and sign up.
    This would provide you with an authorization key which would be used throughout
    the library.
    Store this authorization key in your environment as ```PAYANT_AUTH_KEY```.
    You could also pass this into the base class during initialization.

### Installing

```
pip install -U pypyant
```


Upon completion, try to import the library with

```
import pypayant
```

If the installation was successful, the code above should run without any error.

If an error like ```No module named pypyant``` pops up, then the installation was not succesful.


##Usage

```python
   from pypyant import Client, Payment, Invoice, Products, Misc
   
   
   
   #Client
   
   #Instantitate the Client object to handle all client based actions.  
   client = Client(auth_key=YOUR_AUTH_KEY)
    
    
   #Add a new client
   response = client.add(first_name="Olamilekan",last_name"Wahab",email="olamyy53@gmail.com",phone="000000000000",
                website=None, address=None, state=None, lga=None,
                company_name=None)
    
    # A tuple of 3 elements is always returned if successful or if there
    # was a 404 error.
    #(status_code, status('error'|'success'), message|data)
    
   #Find a new client by passing the client id.
   client.get(client_id=1)
    
   #Edit a client detail
   client.edit(client_id=1,
                 first_name"Olamilekan",
                 last_name="Fadil",
                 email="olamyy53@gmail.com",
                 phone="1111111111",
                 website="github.com/Olamyy",
                 address="Ilab, Obafemi Awolowo University",
                 state="Osun",
                 lga="Ife",
                 company_name="Yes Inc.") 
    
   #Delete a client
   client.delete(client_id)
   
   #Invoice
   
   #Instantitate the Invoice object to handle all client based actions.  
   invoice = Invoice(auth_key=YOUR_AUTH_KEY)  
   
   #Add an invoice for an existing user
   invoice.add(client_id=1,due_date="12/30/2016",fee_bearer="client",
                items={
                        "name": "Website Design",
                        "description": "5 Pages Website plus 1 Year Web Hosting",
                        "unit_cost": "50000.00",
                        "quantity": "1")
   
   #Add an invoice for a new user
   client = {
            "company_name": "Albert Specialist Hospital",
            "first_name": "Albert",
            "last_name": "Jane",
            "email": "jane@alberthospital.com",
            "phone": "+2348012345678",
            "website": "http://www.alberthospital.com",
            "address": "Wase II",
            "state": "37",
            "lga": "782"
            }
   invoice.add(new=True, client, due_date="12/30/2016",fee_bearer="client",
                  items={
                        "name": "Website Design",
                        "description": "5 Pages Website plus 1 Year Web Hosting",
                        "unit_cost": "50000.00",
                        "quantity": "1" 
                        }
    
    
   #Get an invoice
   invoice.get(reference_code="jklmmopujij")
   
   #Send an invoice
   invoice.send(reference_code="abcdefghijk")
   
   #Get an invoice history
   invoice.history(period="custom", start="01/12/2016" , end="31/12/2016")
   
   #Delete an invoice
   invoice.delete(reference_code="abcdefghijk")
   


   #Payment
   
   #Instantitate the Payment object to handle all client based actions.  
   payment = Payment(auth_key=YOUR_AUTH_KEY)
   
   payment.get(reference_code="abcdfgjhi")
   
   payment.history(period="custom", start="01/12/2016" , end="31/12/2016")
   
   
   #Products
   
   
```


## Contributing

To contribute, fork the repo, make your  changes and create a pull request.


##Todo
 Complete ReadME
 More Tests

## Authors

* [Olamilekan Wahab](https://github.com/Olamyy)
* [Biola Oyeniyi](https://github.com/gbozee)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Biola Oyeniyi](https://github.com/gbozee)


