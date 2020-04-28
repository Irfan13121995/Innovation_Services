from __future__ import print_function
import logging
import grpc
import paymentService_pb2
import paymentService_pb2_grpc


def run():
    #replace localhost with external IP of the VM when the service is deployed in Google VM
    #get an HTTP connection to the server

    channel = grpc.insecure_channel("35.204.217.68:5005")
    stub = paymentService_pb2_grpc.PaymentServiceStub(channel)
    
    #Receive personal information customerID 1
    response = stub.GetPersonalInformation(paymentService_pb2.CustomerID(customerID=1))
    logging.info("Customer name is {name} {surname} and he prefers to pay with {method}".format(name=response.name, 
                                                                                       surname=response.surname,
                                                                                       method=response.desiredPaymentMethod))

    #Receive personal information customerID 2
    response = stub.GetPersonalInformation(paymentService_pb2.CustomerID(customerID=2))
    logging.info("Customer name is {name} {surname} and he prefers to pay with {method}".format(name=response.name, 
                                                                                       surname=response.surname,
                                                                                       method=response.desiredPaymentMethod))

    #Receive all payment options
    response = stub.GetPaymentOptions(paymentService_pb2.Empty())
    logging.info(response.name)

    #Check credentials: username doesn't exist.
    response = stub.CheckPaymentCredentials(paymentService_pb2.Credentials(username="omar124", password='jads'))
    logging.info("Paying {result}.".format(result=response.result))

    #Check credentials: username + password combination correct.
    response = stub.CheckPaymentCredentials(paymentService_pb2.Credentials(username="omar123", password='jads'))
    logging.info("Paying {result}.".format(result=response.result))

    #Create a new payment record
    response = stub.CreatePaymentRecord(paymentService_pb2.OrderInformation(customerID=3, orderID=4,amount=70, paid='Succeeded',
                                                            shipmentAddress='Street 7', shipmentCountry='Netherlands',
                                                            name='Dion', surname='van Helvoirt'))
    
    logging.info("Creating the record: {result}.".format(result=response.result))

    #Create a new payment record
    response = stub.SendConfirmation(paymentService_pb2.OrderInformation(customerID=3, orderID=4,amount=70, paid="Succeeded",
                                                            shipmentAddress="Street 7", shipmentCountry="Netherlands",
                                                            name="Dion", surname="van Helvoirt"))
    
    logging.info(response.confirmationMail)



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    run()