import hashlib


def MD5crypto ( string ):
    if string:
        MD5_string = hashlib.md5 ()
        MD5_string.update ( string )
        return MD5_string.hexdigest ()
    return 0