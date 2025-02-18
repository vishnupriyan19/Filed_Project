# Filed_Project
Coding exercise:

Write a Flask Web API with only 1 method called “ProcessPayment” that receives a request like this

-CreditCardNumber(mandatory, string, it should be a valid credit card number)
-CardHolder: (mandatory, string)
-ExpirationDate (mandatory, DateTime, it cannot be in the past)
-SecurityCode (optional, string, 3 digits)
-Amount (mandatoy decimal, positive amount)
The response of this method should be 1 of the followings based on

-Payment is processed: 200 OK
-The request is invalid: 400 bad request
-Any error: 500 internal server error
The payment could be processed using different payment providers (external services)called:

-PremiumPaymentGateway
-ExpensivePaymentGateway
-CheapPaymentGateway.
The payment gateway that should be used to process each payment follows the next set of business rules:

a)If the amount to be paid is less than £20, use CheapPaymentGateway.
b)If the amount to be paid is £21-500, use ExpensivePaymentGateway if available. Otherwise, retry only once with CheapPaymentGateway.
c)If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times in case payment does not get processed.
