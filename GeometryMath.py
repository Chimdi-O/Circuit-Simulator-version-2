import math 

def find_vector(coord1,coord2): # coord1 --> coord2 
    vector = [coord2[0]-coord1[0],coord2[1]-coord1[0]]
    return vector 

def normalise_vector(vector): 
    length = math.sqrt(vector[0]**2+vector[1]**2)
    return length 

def scale_vector(vector,scale_factor): 
    scaled_vector = [vector[0]*scale_factor,vector[1]*scale_factor]
    return scaled_vector 

def find_perp_vector(vector): #perp stands for perpendicular 
    perp_vector = [-vector[1],vector[0]]
    return perp_vector

def rotate_vector(vector,angle): # this can be proved using the double angle formula 
    rotated_vector = [math.cos(angle*vector[0]) - math.sin(angle*vector[1]), 
                      math.sin(angle*vector[0]) + math.cos(angle*vector[1])]
    return rotated_vector

def find_line_coords(vector1,vector2,start_pos): 
    
    mid_pos = [start_pos[0] + vector1[0], [1] + vector1[1]]
    
    top_coord = [mid_pos[0] + vector2[0], mid_pos[1] + vector2[1]]
    bottom_coord = [mid_pos[0] - vector2[0], mid_pos[1] - vector2[1]]

def find_line_equation(start_pos,end_pos): 
    m = (start_pos[1] - end_pos[1])/(start_pos[0]- end_pos[0])
    c = start_pos[1] - m*start_pos[0]
    return [m,c]

def in_or_out_boundary(boundary_coords,point): 
    pass  
    
    

    
