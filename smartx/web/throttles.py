""" Custom throttle class to limit the number of requests per user or IP address """
from rest_framework.throttling import SimpleRateThrottle
from rest_framework.exceptions import Throttled


class ContactFormRateThrottle(SimpleRateThrottle):
    """
    ContactFormRateThrottle is a rate limiting class designed to control the rate at which
    users can submit contact forms. This helps to prevent abuse and spam by limiting the 
    number of submissions a user can make within a specified time period.

    Attributes:
        rate (str): The rate limit as a string, e.g., '5/m' for 5 requests per minute.
        scope (str): The scope of the throttle, typically used to differentiate between 
                     different types of throttles.
    
    Methods:
        allow_request(request, view):
            Determines if the request should be allowed based on the rate limit.
        
        get_cache_key(request, view):
            Generates a unique cache key for the request to track the rate limit.
        
        get_rate():
            Returns the rate limit as a string.
        
        parse_rate(rate):
            Parses the rate limit string into a tuple of (num_requests, period).
    """
    scope = 'contact_form'

    def get_cache_key(self, request, view):
        # Identify the user by their IP address
        return self.get_ident(request)

    def wait(self):
        # Send a custom error response when the rate limit is exceeded
        raise Throttled(detail={
            'status': 'error',
            'message': 'Rate limit exceeded. You can only submit 5 messages per day. Please try again tomorrow.'
        })
