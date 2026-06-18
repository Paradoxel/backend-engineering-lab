import uuid # import for generate unique IDs

# Server side session storage 
sessions = {}

# login function
def login(user_id):
    session_id =str(uuid.uuid4()) # generate a random session id
    sessions[session_id] = {"user_id",user_id}
    return session_id # this goes to browser as cookie


def request(session_id):
    session_data = sessions.get(session_id)  # lookup session in server storage

    if not session_data:  # invalid or expired session
        return "Unauthorized"

    user_id = session_data["user_id"]  # reconstruct user identity from session

    return f"Hello user {user_id}"  # simulate response