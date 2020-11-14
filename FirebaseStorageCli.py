import logging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import os

cred = credentials.Certificate(os.environ['CREDENTIAL_FILE'])
firebase_admin.initialize_app(cred, {
	'storageBucket': os.environ['STORAGE_BUCKET']
})

bucket = storage.bucket()


class FirebaseStorageCli(object):
	def list2file(self, output_path: str) -> None:
		logging.info('[START]list')
		logging.info(f'output_path:{output_path}')
		blobs = bucket.list_blobs()

		with open(output_path, "w", encoding="utf_8") as f:
			for blob in blobs:
				f.write(f'{blob.name}\n')
		logging.info('[END]list')

	def copy(self, src_path: str, dest_path: str):
		logging.info('[START]copy')
		logging.info(f'src_path:{src_path}')
		logging.info(f'dest_path:{dest_path}')
		if src_path == dest_path:
			logging.warning(f'same file. src_path:{src_path}, dest_path:{dest_path}')
			logging.info('[END]copy')
			return
		src_blob = bucket.blob(src_path)
		bucket.copy_blob(src_blob, bucket, dest_path)
		logging.info('[END]copy')

	def delete(self, target_path: str):
		logging.info('[START]delete')
		logging.info(f'target_path:{target_path}')
		bucket.delete_blob(target_path)
		logging.info('[END]delete')
