# sparc-tools
# Overview
Scripts for resolving SPARC tickets

# Running Scripts
- clone repo
- run `pipenv install`
- add in necessary data to empty variables and when in the root of the repo run `python <insert_script_name_here>.py`
        - if you are using python3 and have not added an alias to your .bash_profile you may need to use `python3 
***
## dedupeDeals.py
For a given account, this script finds and deletes duplicate deals. It also creates a .json file with a backup of all the contact's deals before sending the delete requests. As of 01/15/2019:
1) we're defining a duplicate as a Deal belonging to a Contact that has a corresponding Deal with the same `title`, `owner`, and `value`. 
2) we're deleting the newer of the two Deals

### Manual Testing Plan
1) Create a number of duplicate Deals in your personal account.
2) Open dedupeDeals.py and set `account_name`(line 4) and `api_key`(line 5) to the account name and api key of the target account (e.g. for my account with url psmith.activehosted.com, use `psmith` for `account_name` and the key found in Settings -> Developer for the `api_key`). 
3) Save your changes and run `python dedupeDeals.py`. A <account_name>.json file will be created in the directory in which the script is running, and you will see `should delete deal id: <deal_id>` printed to the console.
