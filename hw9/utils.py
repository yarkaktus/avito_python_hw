import csv
import time
from collections import deque
from datetime import datetime
from datetime import timedelta
from os import listdir
from os.path import basename
from os.path import isfile
from os.path import join

import pandas as pd


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if "log_time" in kw:
            name = kw.get("log_name", method.__name__.upper())
            kw["log_time"][name] = int((te - ts) * 1000)
        else:
            print("%r  %2.2f ms" % (method.__name__, (te - ts) * 1000))
        return result

    return timed


def check_overtime(session: deque, max_duration: int, current_dt: datetime) -> bool:
    """
        Проверка на превышение лимита в max_duration с момента первого
        посещенного сайта в сессии.
    """
    first_dt = session[1] if len(session) and session[1] else None
    if first_dt and first_dt + timedelta(minutes=max_duration) < current_dt:
        return True
    return False


@timeit
def prepare_train_set(
    logs_path: str, session_length: int, window_size: int, max_duration: int
) -> pd.DataFrame:
    onlyfiles = [
        join(logs_path, file)
        for file in listdir(logs_path)
        if isfile(join(logs_path, file)) and file.endswith(".csv")
    ]

    sessions = []
    columns = []
    for num in range(1, session_length + 1):
        columns += [
            "site" + str(num),
            "time" + str(num),
        ]
    columns.append("user_id")

    for file in onlyfiles:
        user_id = int(basename(file).split(".")[0].split("user")[1])
        user_deque = deque([user_id], 1)

        data = csv.DictReader(open(file))
        current_session = deque([], session_length * 2)
        session_counter = 0

        for row in data:
            current_dt = datetime.fromisoformat(row["timestamp"])

            save_session = False

            if session_counter == session_length or check_overtime(
                current_session, max_duration, current_dt
            ):
                save_session = True

            if save_session:
                while check_overtime(current_session, max_duration, current_dt) or save_session:
                    if len(current_session) != session_length * 2:
                        count_of_none = session_length * 2 - len(current_session)
                        sessions.append(
                            tuple(
                                tuple(current_session)
                                + tuple(None for _ in range(count_of_none))
                                + tuple(user_deque)
                            )
                        )
                    else:
                        sessions.append(tuple(tuple(current_session) + tuple(user_deque)))

                    save_session = False

                    if window_size != 0 and window_size * 2 < len(current_session):
                        for _ in range(window_size * 2):
                            current_session.popleft()
                    else:
                        current_session.clear()

                session_counter = int(len(current_session) / 2)

            current_session.extend([row["site"], current_dt])
            session_counter += 1

        if session_counter < session_length * 2:  # Забиваем последнюю сессию None
            count_of_none = session_length * 2 - len(current_session)
            sessions.append(
                tuple(
                    tuple(current_session)
                    + tuple(None for _ in range(count_of_none))
                    + tuple(user_deque)
                )
            )

        if window_size == 0:
            break

        while window_size * 2 < len(current_session):
            for _ in range(window_size * 2):
                current_session.popleft()

            count_of_none = session_length * 2 - len(current_session)
            sessions.append(
                tuple(
                    tuple(current_session)
                    + tuple(None for _ in range(count_of_none))
                    + tuple(user_deque)
                )
            )

    df = pd.DataFrame(sessions, columns=columns)
    return df
