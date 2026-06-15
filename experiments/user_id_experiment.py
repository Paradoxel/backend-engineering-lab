import uuid


# MUST be placed after AuthenticationMiddleware
class UserAndRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # next step in Django pipeline

    def __call__(self, request):

        # generate a unique ID for each HTTP request (for tracing/debugging)
        request_id = str(uuid.uuid4())
        request.request_id = request_id  # attach to request object

        # extract user id from authenticated user (if logged in)
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            user_id = None

        request.user_id = user_id  # attach user id to request object

        # pass request to next middleware or view
        response = self.get_response(request)

        # attach request id to response headers (useful for debugging/logging)
        response["X-Request-ID"] = request_id

        # attach user id to response headers (optional, for debugging only)
        if user_id is not None:
            response["X-User-ID"] = str(user_id)

        return response