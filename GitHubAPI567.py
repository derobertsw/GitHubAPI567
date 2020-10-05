# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from typing import List

"""This program outputs a list of the names of the repositories and number of commits in each of the listed 
repositories for a given User ID. """
__author__ = "Will DeRoberts"
__date__ = "September 30th, 2020"


def get_repo_data(user_id: str) -> List:

    validate_user_id(user_id)

    return get_repo_list(user_id, get_repo_name_json(user_id))


def validate_user_id(user_id: str) -> None:
    if len(user_id.strip()) == 0:
        raise ValueError("invalid user_id")


def get_repo_name_json(user_id: str) -> List:
    response = requests.get(
        f"https://api.github.com/users/{user_id}/repos")

    if response.status_code != 200:
        if response.status_code == 400 or response.status_code == 404:
            raise ValueError("invalid user_id")
        else:
            raise RuntimeError("Service Unavailable")

    return response.json()


def get_repo_list(user_id: str, js: List) -> List:
    repo_list = []

    for repo in js:
        count: int = len(requests.get(
            f"https://api.github.com/repos/{user_id}/{repo['name']}/commits").json())
        repo_list.append((repo['name'], count))

    return repo_list


def main() -> None:
    get_repo_data("derobertsw")
    # for repo, count in get_repo_data("nonExistentUserID"):
    #    print(f"Repo {repo} Number of commits: {count}")


if __name__ == '__main__':
    main()
