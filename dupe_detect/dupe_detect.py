from collections import defaultdict
import hashlib
import os
from .throbber import Throbber

class DupeDetector:
    def __init__(self, paths):
        self.paths = paths
        self.duplicates = []

    def __len__(self):
        return len(self.duplicates)

    def delete_last_line(self):
        '''
        Helper function: Deletes previous line
        '''
        CURSOR_UP_ONE = '\x1b[1A' 
        ERASE_LINE = '\x1b[2K'
        HOME = '\r'
        print(HOME + ERASE_LINE,end="",flush=True)

    def chunk_reader(self, fobj, chunk_size=1024):
        '''
        Reads a file in chunks of bytes
        '''
        while True:
            chunk = fobj.read(chunk_size)
            if not chunk:
                return
            yield chunk


    def get_hash(self, filename, first_chunk_only=False, hash=hashlib.sha1):
        '''
        Hashes file
        '''
        hashobj = hash()
        file_object = open(filename, 'rb')

        if first_chunk_only:
            hashobj.update(file_object.read(1024))
        else:
            for chunk in self.chunk_reader(file_object):
                hashobj.update(chunk)
        hashed = hashobj.digest()

        file_object.close()
        return hashed

    def scan(self, hash=hashlib.sha1):
        '''
        Main
        '''
        candidates = defaultdict(list) 
        likely_candidates = defaultdict(list)
        hashes_full = {} 
        throbber = Throbber()
        for path in self.paths:
            for root, dirs, filenames in os.walk(path):
                for filename in filenames:
                    print(f"First pass ",end=str(throbber),flush=True)
                    try:
                        real_path = os.path.realpath(os.path.join(root, filename))
                        if "/dev/" in real_path:
                            continue
                        file_size = os.path.getsize(real_path)
                        candidates[file_size].append(real_path)
                    except OSError:
                        continue
                    throbber.tick()
                    self.delete_last_line()
        print(f"First pass complete,",flush=True)

        throbber.reset()
        for size, files in candidates.items():
            if len(files) < 2:
                continue    

            for filename in files:
                print(f"Second pass ",end=str(throbber),flush=True)
                try:
                    quick_hash = self.get_hash(filename, first_chunk_only=True)
                    likely_candidates[(quick_hash, size)].append(filename)
                except OSError:
                    continue
                throbber.tick()
                self.delete_last_line()
        print(f"Second pass complete.",flush=True)

        throbber.reset()
        retlist = []
        detected = []
        for __, files_list in likely_candidates.items():
            if len(files_list) < 2:
                continue    

            for filename in files_list:
                print(f"Final pass ",end=str(throbber),flush=True)
                try: 
                    full_hash = self.get_hash(filename, first_chunk_only=False)
                    duplicate = hashes_full.get(full_hash)
                    if duplicate and duplicate not in detected:
                        if filename.strip() == duplicate.strip():
                            continue
                        detected.append(filename)
                        retlist.append((filename, duplicate))
                    else:
                        hashes_full[full_hash] = filename
                except OSError:
                    continue
                throbber.tick()
                self.delete_last_line()
        print(f"Final pass complete",flush=True)
        self.duplicates = retlist