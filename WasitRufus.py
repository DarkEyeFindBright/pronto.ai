import sys
from git import Repo
import datetime

dir = sys.argv[1]

# print active branch
print("Active Branch: ", repo.active_branch.name)

# Modified status
status = repo.git.status()
if "modified" in status:
    print("Modified files: True")
else:
    print("Modified files: False")
    
    
# Last Commit
latest_commit = repo.head.commit
time = datetime.datetime.now()
seven_days = datetime.timedelta(days = 7)
if latest_commit.committed_datetime > time - seven_days:
    print("Head commit authored in last week: True")
else:
    print("Head commit authored in last week: False")
    
# check author

if latest_commit.author.name == "Rufus":
    print("Head commit authored by Rufus: True")
else:
    print("Head commit authored by Rufus: False")
