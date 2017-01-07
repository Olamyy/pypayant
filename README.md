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

``` from pypyant.client import Client
    from pypyant.payment import Payment```
    from pypyant.invoice import Invoice```
    from pypyant.products import Products```
    from pypyant.misc import Misc```

    #Instantitate the Client object to handle all client based events.
    
    
    client = Client(auth_key=YOUR_AUTH_KEY)
    
    
    #Add a new client
    client.add("Olamilekan", "Wahab", "olamyy53@gmail.com", "000000000000",
                website=None, address=None, state=None, lga=None,
                company_name=None)
                
                
    #Find a new client by passing the client id.
    client.find(client_id)
    
    #Edit a client detail
    client.edit(3,
                 "Olamilekan",
                 "Fadil",
                 "olamyy53@gmail.com",
                 "1111111111",
                 website="github.com/Olamyy",
                 address="Ilab, Obafemi Awolowo University",
                 state="Osun",
                 lga="Ife",
                 company_name="Yes Inc.") 
    
    #Delete a client
    client.delete(client_id)
```


## Contributing

For contributing, fork the repo, make your  changes and create a pull request.




## Authors

* [Olamilekan Wahab](https://github.com/Olamyy)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Biola Oyeniyi


