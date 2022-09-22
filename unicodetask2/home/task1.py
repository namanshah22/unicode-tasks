#a, b = input("enter 2 numbers: ").split()
def checkbits(a,b):
    dict = {}
    # If no two consecutive bits in a number 'i' are set, i&(i>>1) evaluates to 0
    for i in range(int(a),int(b)):
        if (i & (i >> 1))!=0:
            dict[i]=True
        else:
            dict[i]=False
    return dict

#if __name__ == '__main__':
#    print(checkBits(int(a),int(b)))