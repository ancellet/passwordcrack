# findcrc.def 
import string
#import md5
import hashlib
import base64


def main():    
    findchars()

def find():
    myhash = 'LeE373DA77931BF806DC420C42C2D8D90C164355F9'.lower()

    i = 0
    while i < 10:
        j = 0
        while j < 10:
            k = 0
            while k < 10:
                l = 0
                while l < 10:
                    password = str(i) + str(j) + str(k) + str(l)
                    #temp = str(password)
                    #m = base64.b64encode(password).lower()
                    m = hashlib.sha512(password).hexdigest()
                    if myhash in m:
                        print password
                        print m
                        return
                    #print password
                    #print m
                    l += 1
                k += 1
            j += 1
        i+= 1
    print myhash
    print 'Error: Couldnt find hash'

def findchars():
    myhash = 'OzB394B5FDEF83BECA9BF3718F7EACF966BB084FF5'.lower()
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-='
    length = len(chars)
    a = 0
    while a < length:
        b = 0
        while b <length:
            c = 0
            while c <length:
                d = 0
                while d <length:
                    e = 0
                    while e <length:
                        f = 0
                        while f <length:
                            password = chars[a] + chars[b] + chars[c] +chars[d] + chars[e] +chars[f]
                            crack = hashlib.md5(password).hexdigest()
                            if crack in myhash:
                                print password
                                return
                            f += 1
                        e +=1
                    d+= 1
                c+= 1
            b+=1
        a+=1
    print "Error: Couldnt find hash for chars"




if __name__ == "__main__":
    main();