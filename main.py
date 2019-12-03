import PointInsidePolygonChecker as InsidePolygon
from Plot import Scene
from Plot import  LinesCollection
from Plot import Plot


def initializePolygons():
    # 1 separable
    A = (1, 3)
    B = (4, 1)
    C = (5, 4)
    D = (7, 6)
    E = (3, 6)
    l1 = [A, B]
    l2 = [B, C]
    l3 = [C, D]
    l4 = [D, E]
    l5 = [E, A]
    pointsList1A = [A, B, C, D, E]
    polygon1A = [l1, l2, l3, l3, l4, l5]
    lines1 = LinesCollection(polygon1A, color='green')

    a = (5, 3)
    b = (7, 1)
    c = (11, 4)
    d = (10, 7)
    e = (8, 6)
    l1 = [a, b]
    l2 = [b, c]
    l3 = [c, d]
    l4 = [d, e]
    l5 = [e, a]
    pointsList1B = [a,b,c,d,e]
    polygon1B = [l1, l2, l3, l3, l4, l5]
    lines2 = LinesCollection(polygon1B, color='red')
    scene = Scene([], [lines1, lines2])
    plot = Plot([scene])

    # 2 common edge outside
    A = (1, 4)
    B = (3, 3)
    C = (4, 1)
    D = (6, 5)
    E = (4, 6)
    l1 = [A, B]
    l2 = [B, C]
    l3 = [C, D]
    l4 = [D, E]
    l5 = [E, A]
    pointsList2A = [A, B, C, D, E]
    polygon2A = [l1, l2, l3, l3, l4, l5]
    lines1 = LinesCollection(polygon2A, color='green')

    a = (4, 1)
    b = (9, 1)
    c = (8, 3)
    d = (9, 6)
    e = (6, 5)
    l1 = [a, b]
    l2 = [b, c]
    l3 = [c, d]
    l4 = [d, e]
    l5 = [e, a]
    pointsList2B = [a, b, c, d, e]
    polygon2B = [l1, l2, l3, l3, l4, l5]
    lines2 = LinesCollection(polygon2B, color='red')
    scene = Scene([], [lines1, lines2])
    plot.add_scene(scene)

    # 3 common edge inside
    A = (3, 1)
    B = (6, 2)
    C = (7, 10)
    D = (3, 6)
    E = (1, 4)
    l1 = [A, B]
    l2 = [B, C]
    l3 = [C, D]
    l4 = [D, E]
    l5 = [E, A]
    pointsList3A = [A, B, C, D, E]
    polygon3A = [l1, l2, l3, l3, l4, l5]
    lines1 = LinesCollection(polygon3A, color='green')

    a = (4, 2)
    b = (6, 2)
    c = (7, 10)
    d = (5, 6)
    e = (4, 4)
    l1 = [a, b]
    l2 = [b, c]
    l3 = [c, d]
    l4 = [d, e]
    l5 = [e, a]
    pointsList3B = [a, b, c, d, e]
    polygon3B = [l1, l2, l3, l3, l4, l5]
    lines2 = LinesCollection(polygon3B, color='red')
    scene = Scene([], [lines1, lines2])
    plot.add_scene(scene)

    # 4 common top
    A = (1, 2)
    B = (4, 1)
    C = (5, 4)
    D = (3, 6)
    E = (1, 5)
    l1 = [A, B]
    l2 = [B, C]
    l3 = [C, D]
    l4 = [D, E]
    l5 = [E, A]
    pointsList4A = [A, B, C, D, E]
    polygon4A = [l1, l2, l3, l3, l4, l5]
    lines1 = LinesCollection(polygon4A, color='green')

    a = (6, 1)
    b = (8, 3)
    c = (9, 6)
    d = (6, 5)
    e = (5, 4)
    l1 = [a, b]
    l2 = [b, c]
    l3 = [c, d]
    l4 = [d, e]
    l5 = [e, a]
    pointsList4B = [a, b, c, d, e]
    polygon4B = [l1, l2, l3, l3, l4, l5]
    lines2 = LinesCollection(polygon4B, color='red')
    scene = Scene([], [lines1, lines2])
    plot.add_scene(scene)

    # 5 crossing
    A = (1, 2)
    B = (6, 1)
    C = (5, 5)
    D = (2, 6)
    E = (2, 4)
    l1 = [A, B]
    l2 = [B, C]
    l3 = [C, D]
    l4 = [D, E]
    l5 = [E, A]
    pointsList5A = [A, B, C, D, E]
    polygon5A = [l1, l2, l3, l3, l4, l5]
    lines1 = LinesCollection(polygon5A, color='green')

    a = (3, 2)
    b = (7, 3)
    c = (9, 2)
    d = (9, 5)
    e = (4, 4)
    l1 = [a, b]
    l2 = [b, c]
    l3 = [c, d]
    l4 = [d, e]
    l5 = [e, a]
    pointsList5B = [a, b, c, d, e]
    polygon5B = [l1, l2, l3, l3, l4, l5]
    lines2 = LinesCollection(polygon5B, color='red')
    scene = Scene([], [lines1, lines2])
    plot.add_scene(scene)

    # 6 inside
    A = (1, 1)
    B = (5, 2)
    C = (10, 1)
    D = (8, 6)
    E = (2, 5)
    l1 = [A, B]
    l2 = [B, C]
    l3 = [C, D]
    l4 = [D, E]
    l5 = [E, A]
    pointsList6A = [A, B, C, D, E]
    polygon6A = [l1, l2, l3, l3, l4, l5]
    lines1 = LinesCollection(polygon6A, color='green')

    a = (2, 3)
    b = (5, 3)
    c = (8, 2)
    d = (7, 4)
    e = (5, 5)
    l1 = [a, b]
    l2 = [b, c]
    l3 = [c, d]
    l4 = [d, e]
    l5 = [e, a]
    pointsList6B = [a, b, c, d, e]
    polygon6B = [l1, l2, l3, l3, l4, l5]
    lines2 = LinesCollection(polygon6B, color='red')
    scene = Scene([], [lines1, lines2])
    plot.add_scene(scene)

    plot.draw()

    case1 = (pointsList1A, pointsList1B)
    case2 = (pointsList2A, pointsList2B)
    case3 = (pointsList3A, pointsList3B)
    case4 = (pointsList4A, pointsList4B)
    case5 = (pointsList5A, pointsList5B)
    case6 = (pointsList6A, pointsList6B)
    return case1, case2, case3, case4, case5, case6


def main():
    print("Hello world")
    InsidePolygon.check()
    initializePolygons()


if __name__ == '__main__':
    main()
