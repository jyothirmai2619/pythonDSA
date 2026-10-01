#BINARY SEARCHING
#practice code
# b=[10,11,12,13,14,15]
# def binarysearch(a,target):
#     l=0
#     r=len(a)-1
#     m=l+r//2
#     if a[m]==target:
#         print(f"target found at {m}")
#     elif a[m]<target:
#         l=m
#         m=l+r//2
#         print(f"element found at {m}")
#     else:
#         r=m
#         m=l+r//2
#         print(f'element found at {m}')
# binarysearch(b,13)


#faculty code
b=[10,11,12,13,14,15]
def binarysearch(a,target):
    l=0
    r=len(a)-1
    m=l+r//2
    while l<r:
        if a[m]==target:
            print(f"{target} found at {m}")
            return
        elif a[m]<target:
            l=m
            m=(l+r)//2
        else:
            r=m
            m=(l+r)//2
        print(f'{target} not found')
        return
binarysearch(b,40)