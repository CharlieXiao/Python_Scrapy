import random

def find_fake(lst,start,end):
    if end - start == 1:
        return [start,end]
    if start == end:
        return end
    length = end-start+1
    half = length//2
    aver = lst[end] * half
    if length % 2 == 0:
        weight1 = sum(lst[start:start+half])
        weight2 = sum(lst[start+half:end+1])
        if aver == weight2:
            return find_fake(lst,start,start+half-1)
        else:
            return find_fake(lst,start+half,end)
    else:
        weight1 = sum(lst[start:start+half])
        weight2 = sum(lst[start+half:end])
        if weight1 == weight2:
            return end
        else:
            if weight1 == aver:
                return find_fake(lst,start+half,end)
            else:
                return find_fake(lst,start,start+half-1)




def main():
    L = []
    for i in range(0,100):
        L.append(10)
    temp = random.randint(0,99)
    L[temp] = 9
    print(temp)

    x = find_fake(L,0,99)

    if type(x) == int:
        print(x)
    elif len(L) == 2:
        print("Error")
    else:
        for i in range(len(L)):
            if i != x[0] and i != x[1]:
                if L[i] == L[x[0]]:
                    print(x[1])
                    break
                else:
                    print(x[0])
                    break

main()