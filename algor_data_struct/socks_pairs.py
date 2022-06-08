def sockMerchant(n, ar):
    pairs=0
    allready_id=[]
    for sock in ar:
        cnt=ar.count(sock)
        if sock in allready_id:
            continue
        elif  cnt >= 2:
            a=cnt//2
            pairs+=a
            allready_id.append(sock)
    return pairs

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(9,ar))