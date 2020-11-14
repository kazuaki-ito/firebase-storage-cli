import fire
import logging
from FirebaseStorageCli import FirebaseStorageCli

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
	fire.Fire(FirebaseStorageCli)
