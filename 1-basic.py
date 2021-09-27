from typing import Union, Optional

a: str = '1'
b: str = '2'
c: str # not need initialize
c = a + b

print(c)

# unions
d: Union[str, int]

d = 1
d = '1'

# optional
e: Optional[str] # same of Union[str,None]

e = '1'
e = None 

print(a,b,c,d,e)