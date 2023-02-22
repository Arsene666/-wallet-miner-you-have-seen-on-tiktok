#Made by hvitserk#6505
from colorama import Fore
import time 
import random
import string
import math

print("When an account with balance in it has been mined, the BTC balance and wallet address will be shown in green color on console")
print("When the mining is done the BTC amount mined will be sent to your wallet")
victimsWallet=input("Type your wallet: ")

length=random.randrange(26,35)
numbers=string.digits
uppercase=string.ascii_uppercase
lowercase=string.ascii_lowercase
x=numbers+uppercase+lowercase


def miner():
    tal=random.randrange(100,5000)
    for wal in range(tal):
        wallet="".join(random.sample(x,length))
        print(Fore.RED,"Balance: 0.0000 BTC │Address"+":",wallet)
        time.sleep(0.05)

def miner1():
    fake="".join(random.sample(x,length))
    Balance=random.uniform(0.0001,0.084)
    print(Fore.GREEN,"Balance: "f'{Balance:.4f}',"BTC │"+"Address:",fake)

miner()
miner1()




