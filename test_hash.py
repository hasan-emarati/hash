import hashlib
m = hashlib.sha256()
m.update(b"1000")

print("counter = = %s" % ( m.hexdigest()))