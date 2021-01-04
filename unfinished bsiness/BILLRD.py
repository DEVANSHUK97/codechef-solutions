t = int(str(input()).strip())
for _ in range(t):
    n,k,x,y = (map(int,str(input()).strip().split(' ')))
    if x == y:
        print(f"{n} {n}")
        continue
    right_boundary_x = n
    right_boundary_y = y + (right_boundary_x - x)*1
    
    upper_boundary_x = right_boundary_y
    upper_boundary_y = right_boundary_x
    
    left_boundary_x = n - right_boundary_x
    left_boundary_y = n - right_boundary_y
    
    lower_boundary_x = left_boundary_y
    lower_boundary_y = left_boundary_x
    
    ans_dict  ={1:f"{left_boundary_x} {left_boundary_y}",
                2:f"{upper_boundary_x} {upper_boundary_y}",
                3:f"{right_boundary_x} {right_boundary_y}",
                0:f"{lower_boundary_x} {lower_boundary_y}"}
    
    print(ans_dict[k%4])