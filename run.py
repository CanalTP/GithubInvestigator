from announcer.core import Core as Announcer
from investigator.core import Core as Investigator
import logging

################## Configuration ##################
log_file = './github_investigator.log'
access_token = "XXXXXXX"
file_name = "my_report"
dest_path = '.'
github_organisation = 'my_organisation'
files = {
    'README.md',
    'COPYING',
    'LICENSE'
}
###################################################

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=log_file,
                    filemode='w')

investigator = Investigator(access_token, github_organisation, files)
announcer = Announcer()

investigator.work()
announcer.publish(investigator.get_report(), dest_path, file_name)