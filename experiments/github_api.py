import requests  # HTTP requests library

# GitHub API base endpoint
BASE_URL = "https://api.github.com/users/"

# get username from user input
username = input("User: ")

# send request to GitHub API and convert response to JSON
data = requests.get(BASE_URL + username).json()

# extract user information
name = data.get('name')
followers = data.get("followers")
following = data.get('following')
repos = data.get("public_repos")
location = data.get("location")
avatar_url = data.get("avatar_url")

# print formatted profile data
print("\n--- GITHUB PROFILE ---")
print("Name:", name)
print("Followers:", followers)
print("Following:", following)
print("Public Repos:", repos)
print("Location:", location)
print("Avatar:", avatar_url)