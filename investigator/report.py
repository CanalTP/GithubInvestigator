class Report(object):
    name = None
    files = None
    is_public = False
    is_fork = False

    def __init__(self, repo, files):
        self.name = repo.full_name
        self.is_public = False if repo.private else True
        self.is_fork = True if repo.fork else False
        self.files = files