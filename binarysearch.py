length=int(input())
li=list(map(int,input().strip().split()))
key=int(input())
low=0
high=length-1
while(low<=high ):
    mid=(low+high)//2
    if key==li[mid]:
        
        print(1)
        break
    elif key<li[mid]:
        high=mid-1
        
    elif key>li[mid]:
        low=mid+1
else:
    print(-1)

   
       
   
        
    
        

    



