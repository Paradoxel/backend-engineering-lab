import requests
BASE_URL = "https://api.github.com/users/"

def get_username():
    return input("User: ")

def combine_url():
    return BASE_URL + get_username()


def send_request():
    return requests.get(combine_url())

def handel_request():
    data = send_request()
    if data.status_code!=200:
        print("Error")
        exit()
    else:
        return data
    
def convert_to_json():
    return handel_request().json()


def formater_data(data):
    # extract basic user info safely
    name = data.get("name")
    followers = data.get("followers", 0)
    following = data.get("following", 0)
    repos = data.get("public_repos", 0)
    location = data.get("location")
    avatar = data.get("avatar_url")

    # business logic (simple classification)
    if repos > 50:
        status = "Very Active Developer"
    elif repos > 20:
        status = "Active Developer"
    else:
        status = "Beginner Developer"

    # return formatted structured data
    return {
        "name": name,
        "followers": followers,
        "following": following,
        "repositories": repos,
        "location": location,
        "avatar_url": avatar,
        "status": status
    }

def show_result():
    # get raw data from API
    data = convert_to_json()

    # format data using our logic layer
    formatted = formater_data(data)

    # display clean output
    print("\n========================")
    print("👤 GITHUB PROFILE REPORT")
    print("========================")

    print("Name:", formatted["name"])
    print("Followers:", formatted["followers"])
    print("Following:", formatted["following"])
    print("Public Repos:", formatted["repositories"])
    print("Location:", formatted["location"])
    print("Status:", formatted["status"])
    print("Avatar:", formatted["avatar_url"])

    print("========================")
    
show_result()