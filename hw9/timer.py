from hw9.utils import prepare_train_set

import timeit

t = timeit.Timer('prepare_train_set("train/other_user_logs", 10, 10, 30)', globals=globals())
t.timeit(number=3) / 1600 * 10 ** 3
