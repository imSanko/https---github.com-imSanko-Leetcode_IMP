import math

def calculate_arc_distance(point1, point2):
    straight_line_distance = math.dist(point1, point2)
    arc_distance = (math.pi / 3) * straight_line_distance
    return arc_distance

def calculate_shortest_surface_distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    if z1 == z2:
        return abs(x1 - x2) + abs(y1 - y2)
    elif x1 == x2:
        return abs(z1 - z2) + abs(y1 - y2)
    elif y1 == y2:
        return abs(z1 - z2) + abs(x1 - x2)
    else:
        path1 = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
        return path1

def beetle_travel_distance(n, points):
    total_distance = 0.0
    
    for i in range(1, n):
        point1 = points[i - 1]
        point2 = points[i]
        
        if point1[2] == point2[2]:
            distance = calculate_arc_distance(point1, point2)
        else:
            distance = calculate_shortest_surface_distance
