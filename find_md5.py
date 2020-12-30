import random
import string
from time import sleep
from hashlib import md5

nice_pattern = ['00000000000000000000000000000000', '11111111111111111111111111111111', '22222222222222222222222222222222', '33333333333333333333333333333333', '44444444444444444444444444444444', '55555555555555555555555555555555', '66666666666666666666666666666666', '77777777777777777777777777777777', '88888888888888888888888888888888', '99999999999999999999999999999999', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'cccccccccccccccccccccccccccccccc', 'dddddddddddddddddddddddddddddddd', 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'ffffffffffffffffffffffffffffffff' ]

while(True):
  text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))

  my_hash = md5(text.encode()).hexdigest()

  if my_hash in nice_pattern:
    print("found!!!!")
    print(text,my_hash)
  for i in range(4,10):
    for p in nice_pattern:
      if my_hash[:i]==p[:i]:
        print("found!!!!")
        print(text,my_hash)
  sleep(0.01)