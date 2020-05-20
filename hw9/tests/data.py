from datetime import datetime

DT_FORMAT = "%Y-%m-%d %H:%M:%S"

hard_case = [
    {
        "site1": "vk.com",
        "time1": datetime.strptime("2013-11-15 09:28:17", DT_FORMAT),
        "site2": "oracle.com",
        "time2": datetime.strptime("2013-11-15 09:33:04", DT_FORMAT),
        "site3": "oracle.com",
        "time3": datetime.strptime("2013-11-15 09:52:48", DT_FORMAT),
        "site4": None,
        "time4": None,
        "user_id": 1,
    },
    {
        "site1": "oracle.com",
        "time1": datetime.strptime("2013-11-15 09:52:48", DT_FORMAT),
        "site2": None,
        "time2": None,
        "site3": None,
        "time3": None,
        "site4": None,
        "time4": None,
        "user_id": 1,
    },
    {
        "site1": "geo.mozilla.org",
        "time1": datetime.strptime("2013-11-15 11:37:26", DT_FORMAT),
        "site2": "oracle.com",
        "time2": datetime.strptime("2013-11-15 11:40:32", DT_FORMAT),
        "site3": "google.com",
        "time3": datetime.strptime("2013-11-15 11:40:34", DT_FORMAT),
        "site4": "accounts.google.com",
        "time4": datetime.strptime("2013-11-15 11:40:35", DT_FORMAT),
        "user_id": 1,
    },
    {
        "site1": "google.com",
        "time1": datetime.strptime("2013-11-15 11:40:34", DT_FORMAT),
        "site2": "accounts.google.com",
        "time2": datetime.strptime("2013-11-15 11:40:35", DT_FORMAT),
        "site3": "mail.google.com",
        "time3": datetime.strptime("2013-11-15 11:40:37", DT_FORMAT),
        "site4": "apis.google.com",
        "time4": datetime.strptime("2013-11-15 11:40:40", DT_FORMAT),
        "user_id": 1,
    },
    {
        "site1": "mail.google.com",
        "time1": datetime.strptime("2013-11-15 11:40:37", DT_FORMAT),
        "site2": "apis.google.com",
        "time2": datetime.strptime("2013-11-15 11:40:40", DT_FORMAT),
        "site3": "plus.google.com",
        "time3": datetime.strptime("2013-11-15 11:41:35", DT_FORMAT),
        "site4": None,
        "time4": None,
        "user_id": 1,
    },
    {
        "site1": "plus.google.com",
        "time1": datetime.strptime("2013-11-15 11:41:35", DT_FORMAT),
        "site2": None,
        "time2": None,
        "site3": None,
        "time3": None,
        "site4": None,
        "time4": None,
        "user_id": 1,
    },
]

simple_case2 = [
    {
        "site1": "vk.com",
        "time1": datetime.strptime("2013-11-15 11:28:17", DT_FORMAT),
        "site2": "oracle.com",
        "time2": datetime.strptime("2013-11-15 11:33:04", DT_FORMAT),
        "user_id": 1,
    },
    {
        "site1": "oracle.com",
        "time1": datetime.strptime("2013-11-15 11:34:48", DT_FORMAT),
        "site2": "geo.mozilla.org",
        "time2": datetime.strptime("2013-11-15 11:37:26", DT_FORMAT),
        "user_id": 1,
    },
]

simple_case3 = [
    {
        "site1": "vk.com",
        "time1": datetime.strptime("2013-11-15 09:28:17", DT_FORMAT),
        "site2": "oracle.com",
        "time2": datetime.strptime("2013-11-15 09:33:04", DT_FORMAT),
        "site3": "oracle.com",
        "time3": datetime.strptime("2013-11-15 09:34:48", DT_FORMAT),
        "site4": "geo.mozilla.org",
        "time4": datetime.strptime("2013-11-15 09:37:26", DT_FORMAT),
        "user_id": 1,
    },
    {
        "site1": "oracle.com",
        "time1": datetime.strptime("2013-11-15 09:40:32", DT_FORMAT),
        "site2": None,
        "time2": None,
        "site3": None,
        "time3": None,
        "site4": None,
        "time4": None,
        "user_id": 1,
    },
]
