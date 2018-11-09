#!/usr/bin/env python3

import json
import argparse
from collections import OrderedDict

# Main function that wraps all other functions
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=str, help="Source composer.json")
    parser.add_argument("--repo", "--repository", type=str, help="Select repository")
    parser.add_argument("--url", type=str, help="Updated url")
    args = parser.parse_args()

    edit_zip_url(args.json, args.repo, args.url)

# Changes the .zip URL for a repository
def edit_zip_url(composer_json, repository, url):

    with open(composer_json, "r") as json_file:
        data = json.load(json_file, object_pairs_hook=OrderedDict)

    data['repositories'][repository]['package']['dist']['url'] = url

    with open(composer_json, "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    main()
