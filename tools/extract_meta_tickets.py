# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import re

def extract_issue_links(url):
    # Sends a request to get the page content
    response = requests.get(url)

    # Checks if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

    # Parses the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finds all elements with the 'issue-link' class
    issue_links = soup.find_all(class_='issue-link')

    # Finds all <a> links containing 'pull' in the URL
    pull_request_links = soup.find_all('a', href=True)

    # List to store the extracted data
    issues = []

    # Set to store already processed URLs (to avoid duplicates)
    seen_urls = set()

    # Processes links with the 'issue-link' class (issues)
    for link in issue_links:
        description = link.text.strip()
        href = link.get('href')
        # Removes the #xxx pattern from the description
        description = re.sub(r'#\d+', '', description).strip()

        if href not in seen_urls:
            issues.append({'description': description, 'url': href})
            seen_urls.add(href)  # Adds the URL to the set

    # Processes pull request links (containing 'pull' in the URL)
    for link in pull_request_links:
        href = link['href']
        if 'pull' in href and 'github' in href:  # Captures only GitHub pull requests
            description = link.text.strip()
            # Removes the #xxx pattern from the description
            description = re.sub(r'#\d+', '', description).strip()

            if href not in seen_urls:
                issues.append({'description': description, 'url': href})
                seen_urls.add(href)  # Adds the URL to the set

    return issues

def save_to_csv(issues, filename):
    # Saves the extracted data to a .csv file
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['description', 'url'])
        writer.writeheader()
        for issue in issues:
            writer.writerow(issue)

# Example usage
url = 'https://github.com/ros2/ros2/issues/1149'  # Replace with the desired URL
issues = extract_issue_links(url)

# Saves issues and pull requests to a CSV file
if issues:
    save_to_csv(issues, 'issues_and_pull_requests.csv')
    print("Results saved to 'issues_and_pull_requests.csv'.")
else:
    print("No issues or pull requests found.")
