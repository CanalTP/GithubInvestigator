from pygithub3 import Github
import requests
import logging
from report import Report

class Core(object):
    organizationId = None
    github = None
    report= None
    files = None
    token = None

    def __init__(self, token, organizationId, files):
        self.organizationId = organizationId
        self.github = Github(token=token)
        self.files = files
        self.report = list()
        self.token = token

    def fetch(self, repo):
        file_reports = {}

        for file in self.files:
            url = repo.contents_url.replace('{+path}', file + "?access_token=" + self.token)
            result = requests.get(url)
            file_reports[file] = True if (result.status_code == 200) else False

        self.report.append(Report(repo, file_reports))

        return

    def work(self):
        result = self.github.repos.list_by_org(self.organizationId).all()
        total = len(result)
        i = 1

        for repo in result:
            logging.info(`i` + "/" + `total`)
            self.fetch(repo)
            i += 1

        return

    def get_report(self):
        return self.report
