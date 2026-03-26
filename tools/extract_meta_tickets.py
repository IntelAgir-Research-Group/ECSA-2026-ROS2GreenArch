# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import re

def extract_issue_links(url):
    # Envia uma requisição para obter o conteúdo da página
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code != 200:
        print(f"Falha ao recuperar a página. Código de status: {response.status_code}")
        return []

    # Faz o parsing do conteúdo HTML usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Busca todos os elementos com a classe 'issue-link'
    issue_links = soup.find_all(class_='issue-link')

    # Busca todos os links <a> que contenham 'pull' na URL
    pull_request_links = soup.find_all('a', href=True)

    # Lista para armazenar os dados extraídos
    issues = []

    # Conjunto para armazenar URLs já processados (evitar duplicidades)
    seen_urls = set()

    # Processa os links com a classe 'issue-link' (issues)
    for link in issue_links:
        description = link.text.strip()
        href = link.get('href')
        # Remove o padrão #xxx da descrição
        description = re.sub(r'#\d+', '', description).strip()

        if href not in seen_urls:
            issues.append({'description': description, 'url': href})
            seen_urls.add(href)  # Adiciona o URL ao conjunto

    # Processa os links de pull requests (contêm 'pull' na URL)
    for link in pull_request_links:
        href = link['href']
        if 'pull' in href and 'github' in href:  # Captura apenas os pull requests do GitHub
            description = link.text.strip()
            # Remove o padrão #xxx da descrição
            description = re.sub(r'#\d+', '', description).strip()

            if href not in seen_urls:
                issues.append({'description': description, 'url': href})
                seen_urls.add(href)  # Adiciona o URL ao conjunto

    return issues

def save_to_csv(issues, filename):
    # Salva os dados extraídos em um arquivo .csv
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['description', 'url'])
        writer.writeheader()
        for issue in issues:
            writer.writerow(issue)

# Exemplo de uso
url = 'https://github.com/ros2/ros2/issues/1149'  # Substitua pela URL desejada
issues = extract_issue_links(url)

# Salva os issues e pull requests em um arquivo CSV
if issues:
    save_to_csv(issues, 'issues_and_pull_requests.csv')
    print("Resultados salvos em 'issues_and_pull_requests.csv'.")
else:
    print("Nenhum issue ou pull request encontrado.")
