import os
import sys

INPUT = int( sys.argv[1] )

def pairwise( data ):
    return "".join([ "\\x"+a.encode("hex")+"\\x"+b.encode("hex")  for a,b in zip(data,data[1:])[::2] ])

randomness = os.urandom( INPUT )

print pairwise( randomness )
