# python
import csv
import datetime
import json
from datetime import date
import time
import requests
import re

username = ""  # @param {type:"string"}
password = ""  # @param {type:"string"}

## 입력된 계정/토큰을 출력하고, 정상적으로 API 연결이 되는지 테스트합 겸, API 사용량(Rate Limit 값)을 출력

repos_json = [
	{"repos_no": 1, "repos_url": "https://github.com/SKKUAutoLab/ETSS-08-Data"},
	{"repos_no": 2, "repos_url": "https://github.com/SKKUAutoLab/TSBOW"},
]

## ② Global variables
n_per_page = 100
repos_api_root = "https://api.github.com/repos/"
suffix = datetime.datetime.today().strftime("_%Y-%m-%d_%H%M%S")
gql_query = """query($owner: String!, $name: String!) {
    repository(owner: $owner, name: $name) {
        defaultBranchRef {
            target {
                ... on Commit {
                    history {
                        totalCount
                    }
                }
            }
        }
        issues(states: [CLOSED]) {
            totalCount
        }
        pullRequests(states: [MERGED, CLOSED]) {
            totalCount
        }
    }
}"""

## ③ Result file generation
# repos_result_file_name = "repos-result_github_repo_state_monitor" + suffix + ".csv"
repos_result_file_name = "repos-result_github_repo_state_monitor.csv"
repos_result_file = open(repos_result_file_name, "w", newline="")
repos_result_writer = csv.writer(repos_result_file)
# Write a header on first row of result file
repos_result_writer.writerow(["No.", "Repos. URL", "Stars", "Forks", "Commits", "Closed Issues", "Closed Pull Requests"])

## ④ Alloc. session and save auth. info.
gh_session = requests.Session()
gh_session.auth = (username, password)

# Accumulators for totals
total_star          = 0
total_fork          = 0
total_commits       = 0
total_closed_issues = 0
total_closed_pr     = 0

# Define goals for comparison
goal_star          = 46
goal_fork          = 29
goal_commits       = 612
goal_closed_issues = 0
goal_closed_pr     = 46

def _safe_int(value):
	try:
		return int(value)
	except Exception:
		return 0

for repo in repos_json:

	## ⑥ Generate API link, and validate
	# Build API link, and query to get basic info.
	full_name = repo["repos_url"].replace("https://github.com/","")
	repo_link = repos_api_root + full_name
	repo_info = json.loads(gh_session.get(repo_link).text)

	# From the basic info, check if there's an error message
	if len(repo_info) == 2 and "message" in repo_info:
		print("=================================================================")
		print("[ERROR] %s -> Message : %s" % (repo["repos_url"], repo_info["message"]))
		repos_result_writer.writerow([repo["repos_no"], repo["repos_url"], "ERR", "ERR", "ERR", "ERR", "ERR", repo_info["message"]])
		continue

	# If there's no error, print "TITLE" on console(or result) window for each repo.
	print("=================================================================")
	print("Repos. No = %s, Repos. URL = %s" % (repo["repos_no"], repo["repos_url"]))
	print("-----------------------------------------------------------------")

	## ⑦ Read stats : Total Stars/Forks/Commits/Issues/PullRequests
	# Read Stars & Forks (via REST API)    ## Actually, they're already in the "basic info."
	if "stargazers_count" in repo_info:
		number_of_star = repo_info["stargazers_count"]
	else:
		number_of_star = 0

	if "forks" in repo_info:
		number_of_fork = repo_info["forks"]
	else:
		number_of_fork = 0

	# Read Commits, Closed Issues & Pull Requests
	# Set variables for GraphQL API query
	(owner, name) = full_name.split("/")
	variables = {"owner": "{}".format(owner), "name": "{}".format(name)}

	# Send request and Get response(=result)
	request = gh_session.post('https://api.github.com/graphql', json={'query': gql_query, 'variables': variables})
	if request.status_code == 200:
		result = request.json()
		number_of_commits = result["data"]["repository"]["defaultBranchRef"]["target"]["history"]["totalCount"]
		number_of_closed_issues = result["data"]["repository"]["issues"]["totalCount"]
		number_of_closed_pullRequests = result["data"]["repository"]["pullRequests"]["totalCount"]
	else:
		number_of_commits = "ERR"
		number_of_closed_issues = "ERR"
		number_of_closed_pullRequests = "ERR"

	## ⑧ Print and save results
	print("S= %s,\tF= %s,\tC= %s,\tI= %s,\tP= %s" % (number_of_star, number_of_fork, number_of_commits, number_of_closed_issues, number_of_closed_pullRequests))
	repos_result_writer.writerow([repo["repos_no"], repo["repos_url"], number_of_star, number_of_fork, number_of_commits, number_of_closed_issues, number_of_closed_pullRequests])

	# Update totals (treat non-numeric as 0)
	total_star += _safe_int(number_of_star)
	total_fork += _safe_int(number_of_fork)
	total_commits += _safe_int(number_of_commits)
	total_closed_issues += _safe_int(number_of_closed_issues)
	total_closed_pr += _safe_int(number_of_closed_pullRequests)

## ⑨ After all loops, report API rate limit status
report = json.loads(gh_session.get("https://api.github.com/rate_limit").text)
print("=================================================================")
print("[REST API] Limit = %s, Used = %s, Remaining = %s" % (report["resources"]["core"]["limit"], report["resources"]["core"]["used"], report["resources"]["core"]["remaining"]))
print("     * Reset at: %s" % time.ctime(report["resources"]["core"]["reset"]))
print("[GraphQL API] Limit = %s, Used = %s, Remaining = %s" % (report["resources"]["graphql"]["limit"], report["resources"]["graphql"]["used"], report["resources"]["graphql"]["remaining"]))
print("     * Reset at: %s" % time.ctime(report["resources"]["graphql"]["reset"]))

# Print and write totals row
print("=================================================================")
print("TOTALS: S= %s,\tF= %s,\tC= %s,\tI= %s,\tP= %s" % (total_star, total_fork, total_commits, total_closed_issues, total_closed_pr))
print("DIFF:   S= %s,\tF= %s,\tC= %s,\tI= %s,\tP= %s" % (goal_star-total_star, goal_fork-total_fork, goal_commits-total_commits, goal_closed_issues-total_closed_issues, goal_closed_pr-total_closed_pr))
repos_result_writer.writerow(["Total", "", total_star, total_fork, total_commits, total_closed_issues, total_closed_pr])

############# FINISHED #############
## Close all sessions
gh_session.close()
repos_result_file.close()
