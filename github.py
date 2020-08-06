import requests
import requests_cache

requests_cache.install_cache('repo-cache', expire_after=60*60*24)

class User():
    def __init__(self, user):
        self.user=user
    def info(self):
        response = requests.get(f'https://api.github.com/users/{self.user}')
        response.raise_for_status()
        return response.json()
    def starred(self):
        response = requests.get(f'https://api.github.com/users/{self.user}/starred')
        response.raise_for_status()
        return response.json()
    def repos(self):
        response = requests.get(f'https://api.github.com/users/{self.user}/repos')
        response.raise_for_status()
        return response.json()
    def following(self):
        response = requests.get(f'https://api.github.com/users/{self.user}/subscriptions')
        response.raise_for_status()
        return response.json()

def readme(owner_repo):
    response = requests.get(f'https://api.github.com/repos/{owner_repo}/readme')
    response.raise_for_status()
    return response.json()