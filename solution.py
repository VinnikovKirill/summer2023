import gmpy2
from Crypto.Util.number import long_to_bytes, bytes_to_long
import time

n = 12189464288007059657184858632825479990912616419482466046617619319388181010121359489739982536798361842485210016303524715395474637570227926791570158634811951043352789232959763417380155972853016696908995809240738171081946517881643416715486249
e = 65537
c = 10093874086170276546167955043813453195412484673031739173390677430603113063707524122014352886564777373620029541666833142412009063988439640569778321681605225404251519582850624600712844557011512775502356036366115295154408488005375252950048742

#Число p находится в [2^255, 2^256], бинарным поиском подбираем p и q

first = gmpy2.next_prime(2**255)
last = gmpy2.next_prime(2**256)
p = -1
q = -1

start_time = time.time()
while (first <= last) and (p == -1):
    p0 = gmpy2.next_prime((first+last)//2)
    q0 = int(gmpy2.digits(p0, 3))
    N=p0*q0
    if (N == n):
        p = p0
        q = q0
    else:
        if (N<n):
            first = p0 +1
        else:
            last = p0 -1
finish_time = time.time()

phi=(p-1)*(q-1)
d=pow(e,-1,phi)
m=int(pow(c,d,n))

t=long_to_bytes(m)

print('p=',p,'\nq=',q,'\n\nm=',m,'\n\nm=',t)
print(finish_time - start_time)




