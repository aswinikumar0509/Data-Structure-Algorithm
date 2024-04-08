def mCoin(coin,val):

    if val==0:
        return 0
    n = len(coin)
    res = -1
    for i in range(n):
        if (coin[i]<=val):
            sub_res = mCoin(coin,val-coin[i])
            if sub_res!=-1:
                if res==-1 or (sub_res+1)<res:
                    res = sub_res+1

    return res

coin = [25,10,5]
val=20

print(mCoin(coin,val))