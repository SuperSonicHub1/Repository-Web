import github
import base64
import re
import os
import json


def get_img(owner_repo):
    readme_img = []
    try:
        content = base64.b64decode(github.readme(owner_repo)['content']).decode("utf-8", "strict")
        regex = r"(http(|s):.*\.(jpeg|png|jpg|gif))"
        readme_img = re.findall(regex, content, re.MULTILINE)
    except:
        pass
    
    if readme_img:
        return readme_img[0][0]
    else:
        return ''
        
def get_repos(user):
    user = github.User(user)

    colors = json.load(open('colors.json'))

    starred = user.starred() 
    repos = user.repos()
    subscriptions = user.following()
    
    props = {}
    props['profile'] = user.info()
    props['length'] = len(starred + repos + subscriptions)
    props['starred'] = []
    props['repos'] = []
    props['subscriptions'] = []

    for repo in starred:
        try:
            color = colors.get(repo['language'])['color']
        except:
            color = '#6083b6'
        props['starred'].append({
            "name": repo['name'],
            "author": repo['owner']['login'],
            "author_link": repo['owner']['html_url'],
            "repo_link": repo['html_url'],
            "repo_description": repo['description'],
            "language": str(repo['language']), 
            "color": color,
            "forks": repo['forks'],
            "watchers": repo['watchers'],
            "stars": repo['stargazers_count'],
            "img": get_img(repo['full_name'])
        })
    for repo in repos:
        try:
            color = colors.get(repo['language'])['color']
        except:
            color = '#6083b6'
        props['repos'].append({
            "name": repo['name'],
            "author": repo['owner']['login'],
            "author_link": repo['owner']['html_url'],
            "repo_link": repo['html_url'],
            "repo_description": repo['description'],
            "language": str(repo['language']), 
            "color": color,
            "forks": repo['forks'],
            "watchers": repo['watchers'],
            "stars": repo['stargazers_count'],
            "img": get_img(repo['full_name'])
        })
    for repo in subscriptions:
        try:
            color = colors.get(repo['language'])['color']
        except:
            color = '#6083b6'
        props['subscriptions'].append({
            "name": repo['name'],
            "author": repo['owner']['login'],
            "author_link": repo['owner']['html_url'],
            "repo_link": repo['html_url'],
            "repo_description": repo['description'],
            "language": str(repo['language']), 
            "color": color,
            "forks": repo['forks'],
            "watchers": repo['watchers'],
            "stars": repo['stargazers_count'],
            "img": get_img(repo['full_name'])
        })
    return props