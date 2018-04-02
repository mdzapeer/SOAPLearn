import random
from datetime import datetime

random.seed(int(datetime.now().strftime("%f")) * 1000)
rn1=random.random() * 1000000000

print (int(rn1))
