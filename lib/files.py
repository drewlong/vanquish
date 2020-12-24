import os.path
import hashlib

def file_hash(sum, type, path):
  BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
  if type == 'md5':
    hash = hashlib.md5()
  elif type == 'sha1':
    hash = hashlib.sha1()
  elif type == "sha256":
    hash = hashlib.sha256()

  with open(path, 'rb') as f:
      while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        hash.update(data)
  return sum == hash.hexdigest()

def file_path(path):
  return os.path.isfile(path)
