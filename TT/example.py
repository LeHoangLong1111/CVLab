def NumofPaPer(T):
    print("Okey: ",T)

if __name__ == "__main__":
    c=10**9
    print('Enter T is integer: ')
    T = int(input())
    flag = (T>=1 and T<=2)
    print('flag= ', flag)
    while (not flag):
        print("----------")
        print('Wrong!!')
        print("T in 1<=T<=2")
        print('Enter T is integer again: ')
        T = int(input())
        flag = T>=1 and T<=2
    # NumofPaPer(T)