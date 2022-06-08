def countingValleys(steps, path):
    final_stp=0
    results=0
    for i in range(steps):
        if path[i] == "D":
            final_stp-=1

        elif path[i] == "U":
            final_stp+=1
            if final_stp ==0:
                results+=1

    return results





    # for elem in path:
    #     if elem == "D":
    #         final_stp-=1
    #     elif elem == "U":
    #         final_stp+=1
    # return abs(final_stp)


s=12
a="DDUUDDUDUUUD"
print(countingValleys(s,a))
