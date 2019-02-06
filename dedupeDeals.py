import requests
import json

account_name = ''
api_key = ''
headers = {'Content-Type': 'application/json', 'Api-Token': api_key}

def get_values_from_api(account_name, headers, endpoint, limit, offset, filter_string):
    url = 'https://{0}.api-us1.com/api/3/{1}?limit={2}&offset={3}&{4}'.format(account_name, endpoint, limit, offset, filter_string)
    print(url)
    response = requests.get(url, headers=headers)
    return response

def delete_from_api(account_name, headers, endpoint, id):
    url = 'https://{0}.api-us1.com/api/3/{1}/{2}'.format(account_name, endpoint, id)
    response = requests.delete(url, headers=headers)
    return response

def get_deals(account_name, headers, endpoint, limit, offset, filter_string):
    all_deals = []
    first_page = get_values_from_api(account_name, headers, endpoint, limit, offset, filter_string).json()
    all_deals.extend(list(map(lambda x: x, first_page['deals'])))
    print(len(all_deals))
    #page through results and add to all_deals until we have all the deals
    while len(all_deals) != int(first_page['meta']['total']):
        offset = offset + limit
        page = get_values_from_api(account_name, headers, endpoint, limit, offset, filter_string).json()
        all_deals.extend(list(map(lambda x: x, page['deals'])))
        print(len(all_deals))
    return all_deals

#get all the deals
all_deals = get_deals(account_name, headers, 'deals', 100, 0, '')
#grab all the unique contact ids from the deals
contact_ids = {s['contact'] for s in all_deals}
#for all the contact_ids, put the deals with matching contact ids in a list in matches
matches = []
for id in contact_ids:
    matches.append([deal for deal in all_deals if deal['contact'] == id])
#if there are only two matches with the same contact id, these are probably duplicates
probable_dupes = [match for match in matches if len(match) == 2]
#for each of the probable duplicates, if they have the same title, owner, and value, grab the deal with the higher id and delete it
for match in probable_dupes:
    if match[0]['title'] == match[1]['title'] and match[0]['owner'] == match[1]['owner'] and match[0]['value'] == match[1]['value']:
        higher_id = max(int(match[0]['id']), int(match[1]['id']))
        print('should delete deal id: {0}'.format(higher_id))
        # delete_from_api(account_name, headers, deals, higher_id)
