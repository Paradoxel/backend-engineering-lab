import uuid
import logging

# logger for this file
logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        # next middleware or view
        self.get_response = get_response

    def __call__(self, request):

        # create request id
        request_id = str(uuid.uuid4())
        request.request_id = request_id

        # get user id if logged in
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            user_id = None

        request.user_id = user_id

        # log request start
        logger.info(
            f"START request_id={request_id} user_id={user_id} path={request.path}"
        )

        # call next layer
        response = self.get_response(request)

        # log request end
        logger.info(
            f"END request_id={request_id} user_id={user_id} status={response.status_code}"
        )

        # attach headers (debug only)
        response["X-Request-ID"] = request_id

        if user_id is not None:
            response["X-User-ID"] = str(user_id)

        return response