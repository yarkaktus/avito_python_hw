import os

from utils import prepare_train_set

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    path = os.path.join(BASE_DIR, "train/other_user_logs")
    prepare_train_set(path, 10, 10, 30)
