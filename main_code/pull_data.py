

from pycricket import cricket
import json
c = cricket.Cricket()
matches = c.query(mtype=['ODI'],team1=['India'],startdate='2017-01-01')
for match in matches:
	scorecard = c.scorecard(match['id'])
	print json.dumps(scorecard,indent=4)