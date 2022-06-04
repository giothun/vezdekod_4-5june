import json
import requests
import sys


for handle in sys.stdin:
    handle = handle.strip()
    url = "https://codeforces.com/api/user.status?handle="+handle+"&from=1&count=1000000000"
    user_info = requests.get(url)

    # print(handle)
    user_dict= user_info.json()['result']
    used_dict = {}
    cnt = 0
    for i in range(len(user_dict)):
        contestId = user_dict[i]['problem']['contestId']
        used_dict[contestId] = []
    for i in range(len(user_dict)):
        contestId = user_dict[i]['problem']['contestId']
        index = user_dict[i]['problem']['index']
        if(index not in used_dict[contestId]):
            used_dict[contestId].append(index)
            cnt+=1
    print(handle, ":",cnt)