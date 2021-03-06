# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import paymentService_pb2 as paymentService__pb2


class PaymentServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPersonalInformation = channel.unary_unary(
                '/ordermgt.PaymentService/GetPersonalInformation',
                request_serializer=paymentService__pb2.CustomerID.SerializeToString,
                response_deserializer=paymentService__pb2.CustomerInformation.FromString,
                )
        self.GetPaymentOptions = channel.unary_unary(
                '/ordermgt.PaymentService/GetPaymentOptions',
                request_serializer=paymentService__pb2.Empty.SerializeToString,
                response_deserializer=paymentService__pb2.PaymentOptions.FromString,
                )
        self.CheckPaymentCredentials = channel.unary_unary(
                '/ordermgt.PaymentService/CheckPaymentCredentials',
                request_serializer=paymentService__pb2.Credentials.SerializeToString,
                response_deserializer=paymentService__pb2.Status.FromString,
                )
        self.CreatePaymentRecord = channel.unary_unary(
                '/ordermgt.PaymentService/CreatePaymentRecord',
                request_serializer=paymentService__pb2.OrderInformation.SerializeToString,
                response_deserializer=paymentService__pb2.Succeeded.FromString,
                )
        self.SendConfirmation = channel.unary_unary(
                '/ordermgt.PaymentService/SendConfirmation',
                request_serializer=paymentService__pb2.OrderInformation.SerializeToString,
                response_deserializer=paymentService__pb2.MailMessage.FromString,
                )


class PaymentServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetPersonalInformation(self, request, context):
        """Receive personal information of paying customer
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPaymentOptions(self, request, context):
        """Receive payment options (banks)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckPaymentCredentials(self, request, context):
        """Check payment credentials
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePaymentRecord(self, request, context):
        """Create payment record with id and (for now) untried.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendConfirmation(self, request, context):
        """Send confirmation to customer
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PaymentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPersonalInformation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPersonalInformation,
                    request_deserializer=paymentService__pb2.CustomerID.FromString,
                    response_serializer=paymentService__pb2.CustomerInformation.SerializeToString,
            ),
            'GetPaymentOptions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPaymentOptions,
                    request_deserializer=paymentService__pb2.Empty.FromString,
                    response_serializer=paymentService__pb2.PaymentOptions.SerializeToString,
            ),
            'CheckPaymentCredentials': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckPaymentCredentials,
                    request_deserializer=paymentService__pb2.Credentials.FromString,
                    response_serializer=paymentService__pb2.Status.SerializeToString,
            ),
            'CreatePaymentRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePaymentRecord,
                    request_deserializer=paymentService__pb2.OrderInformation.FromString,
                    response_serializer=paymentService__pb2.Succeeded.SerializeToString,
            ),
            'SendConfirmation': grpc.unary_unary_rpc_method_handler(
                    servicer.SendConfirmation,
                    request_deserializer=paymentService__pb2.OrderInformation.FromString,
                    response_serializer=paymentService__pb2.MailMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ordermgt.PaymentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PaymentService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetPersonalInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ordermgt.PaymentService/GetPersonalInformation',
            paymentService__pb2.CustomerID.SerializeToString,
            paymentService__pb2.CustomerInformation.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPaymentOptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ordermgt.PaymentService/GetPaymentOptions',
            paymentService__pb2.Empty.SerializeToString,
            paymentService__pb2.PaymentOptions.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckPaymentCredentials(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ordermgt.PaymentService/CheckPaymentCredentials',
            paymentService__pb2.Credentials.SerializeToString,
            paymentService__pb2.Status.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreatePaymentRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ordermgt.PaymentService/CreatePaymentRecord',
            paymentService__pb2.OrderInformation.SerializeToString,
            paymentService__pb2.Succeeded.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendConfirmation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ordermgt.PaymentService/SendConfirmation',
            paymentService__pb2.OrderInformation.SerializeToString,
            paymentService__pb2.MailMessage.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
