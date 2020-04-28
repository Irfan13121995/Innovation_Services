from concurrent import futures
import logging
import grpc
import paymentService_pb2
import paymentService_pb2_grpc
import pandas as pd 
from csv import writer

class PaymentService(paymentService_pb2_grpc.PaymentServiceServicer):
    personalInformation = {}

    #def __init__(self):
    #    self.personalInformation = pd.read_csv("PersonalInformation.csv").set_index('customerID').to_dict(orient="index")
    
    ##Receive personal information of paying customer
    def GetPersonalInformation(self, request, context):
        info = pd.read_csv("PersonalInformation.csv").set_index('customerID').to_dict(orient="index")[request.customerID]
        #info = self.personalInformation[request.customerID]

        return paymentService_pb2.CustomerInformation(customerID=request.customerID, 
                                                      name=info["name"],
                                                      surname=info["surname"],
                                                      address=info["address"],
                                                      country=info["country"],
                                                      postcode=info["postcode"],
                                                      phonenumber=info["phonenumber"],
                                                      province=info["province"],
                                                      desiredPaymentMethod=info["desiredPaymentMethod"])

    def GetPaymentOptions(self, request, context):

       return paymentService_pb2.PaymentOptions(name=[method for method in pd.read_csv("PaymentMethods.csv")['Methods'].values])

    def CheckPaymentCredentials(self, request, context):

        credentials = pd.read_csv("Credentials.csv").set_index('username').to_dict(orient="index")

        if request.username in credentials.keys():
            
            if request.password==credentials[request.username]["password"]:
                
                return paymentService_pb2.Status(result="Succeeded")
        
        return paymentService_pb2.Status(result="Failed")

    def CreatePaymentRecord(self, request, context):
        
        row = [request.customerID, request.orderID, request.amount, request.paid, 
            request.name, request.surname, request.shipmentAddress, request.shipmentCountry]
        
        try:
        

            with open("Payments.csv", 'a', newline='') as write_obj:
                # Create a writer object from csv module
                csv_writer = writer(write_obj)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(row)

            return paymentService_pb2.Succeeded(result=True)

        except:
            return paymentService_pb2.Succeeded(result=False)

    def SendConfirmation(self, request, context):
        mailMessage = """Dear {name} {surname},\n
                        \n

                         The payment for your order with order ID {orderID} {paymentResult}. \n
                         The amount paid for was {amount} and will be shipped to {address}, {country}. \n
                         \n
                         
                         Kind regards,\n
                         \n
                         The Amazon Team""".format(name=request.name, surname=request.surname, orderID=request.orderID,
                         paymentResult=request.paid, amount=request.amount, address=request.shipmentAddress, 
                         country=request.shipmentCountry)

        return paymentService_pb2.MailMessage(confirmationMail=mailMessage)
        

def serve():
    # Create a gRPC server instance and register the service
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    paymentService_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)
    logging.info("PaymentService Deployed")
    server.add_insecure_port("[::]:5005") #HTTP Transport
    server.start()
    logging.info("Server Started")
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    serve()

