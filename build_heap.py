# python3
# python3

import sys
import threading

def build_heap(data):
    swaps = []
    temp=0
    flag=False
    notleaf = int(len(data)/2-1)
    while not flag:
        
        if notleaf>=0:
            if data[notleaf]>data[notleaf*2+1] or data[notleaf]>data[notleaf*2+1]:
                if data[notleaf*2+2] > data[notleaf*2+1]:
                    
                    swaps.append((notleaf,notleaf*2+1))
                    temp = data[notleaf]
                    data[notleaf] = data[notleaf*2+1]
                    data[notleaf*2+1] = temp
                else:
                    
                    swaps.append((notleaf,notleaf*2+2))
                    temp = data[notleaf]
                    data[notleaf] = data[notleaf*2+2]
                    data[notleaf*2+2] = temp
                notleaf-=1
                continue
            if notleaf == 0: flag = True
        else: notleaf = int(len(data)/2-1)        
                
            
        
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    # input from keyboard
    print("I or F")
    StrOrFile = input()
    print("n number:")
    n = int(input())
    if StrOrFile[0] == 'F':
        file_name = input()
        text1 = (open( sys.path[0]+ "/test/" + file_name, "r").read()).split("\n")
        data=list(map(int, text1[0].split()))
    elif StrOrFile[0] == 'I':
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

