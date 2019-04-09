# -*- coding:utf-8 -*-


data = []
rows = [["ack", 1, 100], ["ack", "", 1101], ["udp", 3, 200], ["udp", 3, 201]]
"""
row_dict = {"ack": [{"start_time": 1, "total_bytes": 100}, {"start_time": 2, "total_bytes": 101}],
            "udp": [{"start_time": 3, "total_bytes": 200}, {"start_time": 3, "total_bytes": 201}]}

"""
row_dict = {}
for row in rows:
    if not row_dict.get(row[0]):
        row_dict.setdefault(row[0], [{"start_time": row[1], "total_bytes": row[2]}])
        print(row_dict)
    else:
        row_dict[row[0]].append({"start_time": row[1], "total_bytes": row[2]})

result = {}
for item in row_dict.keys():
    result["data"] = row_dict[item]
    result["name"] = item
    data.append(result)
print({"status": 1, "data": data})


