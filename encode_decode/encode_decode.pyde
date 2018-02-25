from alphabet import *

#print decodings
#print encodings

message = "why must the world be overwise, in counting all its tears and sighs"
#print message

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
def groupings(l, n):
    return list(chunks(l,n))

def encode(message):
    acc = ''
    
    for c in message:
        acc += encodings[c]  
    
    return int(acc)

encoding = encode(message)
print encoding

def decode(encoding):
    acc = ''
    keys = groupings(str(encoding),3)
        
    for key in keys:
        acc += decodings[key]  
    
    return acc

output = decode(encoding)
print output

# print decodings['101']