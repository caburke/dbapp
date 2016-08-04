from datetime import datetime
import json

def table_to_json(table):

    ll = [[el.isoformat() if isinstance(el, datetime) else el for el in row]
        for row in table]

    data = {'data': ll}

    return json.dumps(data)
