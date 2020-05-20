from utils import prepare_train_set

import timeit

t = timeit.Timer('prepare_train_set("train/other_user_logs", 10, 10, 30)', globals=globals())
print(t.timeit(number=1) / 1 * 10 ** 3)
