
import cricket
import json
import ast
import pandas as pd
import numpy as np


def get_info_from_json(x):
	curr_arr = np.empty(shape = (1, 6), dtype='object')
	curr_arr[0][0] = x['name']
	curr_arr[0][1] = x['runs']
	curr_arr[0][2] = x['balls']
	curr_arr[0][3] = x['fours']
	curr_arr[0][4] = x['six']
	curr_arr[0][5] = x['dismissal']
	return curr_arr


c = cricket.Cricket()
matches = c.query(mtype=['ODI'],team1=['India'],startdate='2017-01-01')
match = matches[0]
#print(match)
scorecard = c.scorecard(match['id'])
#print(scorecard)
match_info = ast.literal_eval(json.dumps(scorecard,indent=4))
print(json.dumps(match_info['innings'][0]['batting'][0]))
curr_innings = match_info['innings'][0]['batting']

info = np.empty(shape = (0, 6), dtype='object')
for i in range(len(curr_innings)):
	curr_arr = get_info_from_json(curr_innings[i])
	info = np.concatenate((info, curr_arr))

info = pd.DataFrame(info, columns = ['name', 'runs', 'balls', 'fours', 'six', 'dismissal'])
print(info.head())