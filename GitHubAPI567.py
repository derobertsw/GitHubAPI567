# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from typing import List

"""This program outputs a list of the names of the repositories and number of commits in each of the listed 
repositories for a given User ID. """
__author__ = "Will DeRoberts"
__date__ = "September 30th, 2020"


def get_repo_data(user_id: str) -> List:
    repo_list = []

    validate_user_id(user_id)

    response = requests.get(
        f"https://api.github.com/users/{user_id}/repos")

    if response.status_code != 200:
        if response.status_code == 400:
            raise ValueError("invalid user_id")
        else:
            raise RuntimeError("Service Unavailable")
        exit()

    js = response.json()

    for repo in js:
        count: int = len(requests.get(
            f"https://api.github.com/repos/{user_id}/{repo['name']}/commits").json())
        repo_list.append((repo['name'], count))

    return repo_list


def validate_user_id(user_id:str) -> None:
    if len(user_id.strip()) == 0:
        raise ValueError("invalid user_id")

def main() -> None:
    print(get_repo_data("derobertsw"))

    for repo, count in get_repo_data("derobertsw"):
        print(f"Repo {repo} Number of commits: {count}")


if __name__ == '__main__':
    main()
