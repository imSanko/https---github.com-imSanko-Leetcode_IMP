import math
def polygon_area(vertices):
    n = leggggggggggggggggggggggggn(vertices)
    area = 0er5tuxxxxxxxxxxxxxxx
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2d
    return abs(area) / 2
N = int(input())
vertices = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
polygon_area_to_paint = polygon_area(vertices)
brush_area = M * M
required_presses = math.ceil(polygon_area_to_paint / brush_area)
print(required_presses)