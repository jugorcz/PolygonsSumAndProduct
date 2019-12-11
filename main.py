from Plot import Scene
from Plot import LinesCollection
from Plot import PointsCollection
from Plot import Plot
import PointInsidePolygonChecker as InsidePolygon
import sys


def initialize_polygons(case):
    plot = Plot([])

    if case == 1:
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
        points_list1_a = [A, B, C, D, E]
        polygon1_a = [l1, l2, l3, l3, l4, l5]
        points1 = PointsCollection(points_list1_a, color="blue")
        lines1 = LinesCollection(polygon1_a, color='green')

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
        points_list1_b = [a, b, c, d, e]
        polygon1_b = [l1, l2, l3, l3, l4, l5]
        points2 = PointsCollection(points_list1_b, color="orange")
        lines2 = LinesCollection(polygon1_b, color='red')

        scene = Scene([points1, points2], [lines1, lines2])
        plot.add_scene(scene)
        case_points = (points_list1_a, points_list1_b)
        case_polygon = (polygon1_a, polygon1_b)

    elif case == 2:
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
        points_list2_a = [A, B, C, D, E]
        polygon2_a = [l1, l2, l3, l3, l4, l5]
        points1 = PointsCollection(points_list2_a, color="blue")
        lines1 = LinesCollection(polygon2_a, color='green')

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
        points_list2_b = [a, b, c, d, e]
        polygon2_b = [l1, l2, l3, l3, l4, l5]
        points2 = PointsCollection(points_list2_b, color="orange")
        lines2 = LinesCollection(polygon2_b, color='red')

        scene = Scene([points1, points2], [lines1, lines2])
        plot.add_scene(scene)
        case_points = (points_list2_a, points_list2_b)
        case_polygon = (polygon2_a, polygon2_b)

    elif case == 3: #  common top
        A = (1, 2)
        B = (4, 1)
        C = (5, 4)
        D = (3, 6)
        E = (2, 5)
        l1 = [A, B]
        l2 = [B, C]
        l3 = [C, D]
        l4 = [D, E]
        l5 = [E, A]
        points_list4_a = [A, B, C, D, E]
        polygon4_a = [l1, l2, l3, l3, l4, l5]
        points1 = PointsCollection(points_list4_a, color="blue")
        lines1 = LinesCollection(polygon4_a, color='green')

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
        points_list4_b = [a, b, c, d, e]
        polygon4_b = [l1, l2, l3, l3, l4, l5]
        points2 = PointsCollection(points_list4_b, color="orange")
        lines2 = LinesCollection(polygon4_b, color='red')

        scene = Scene([points1, points2], [lines1, lines2])
        plot.add_scene(scene)
        case_points = (points_list4_a, points_list4_b)
        case_polygon = (polygon4_a, polygon4_b)

    elif case == 4: # crossing
        A = (1, 2)
        B = (6, 1)
        C = (5, 5)
        D = (2, 6)
        E = (3, 4)
        l1 = [A, B]
        l2 = [B, C]
        l3 = [C, D]
        l4 = [D, E]
        l5 = [E, A]
        points_list5_a = [A, B, C, D, E]
        polygon5_a = [l1, l2, l3, l3, l4, l5]
        points1 = PointsCollection(points_list5_a, color="blue")
        lines1 = LinesCollection(polygon5_a, color='green')

        a = (3, 2)
        b = (7, 3)
        c = (10, 2)
        d = (9, 5)
        e = (4, 4)
        l1 = [a, b]
        l2 = [b, c]
        l3 = [c, d]
        l4 = [d, e]
        l5 = [e, a]
        points_list5_b = [a, b, c, d, e]
        polygon5_b = [l1, l2, l3, l3, l4, l5]
        points2 = PointsCollection(points_list5_b, color="orange")
        lines2 = LinesCollection(polygon5_b, color='red')

        scene = Scene([points1, points2], [lines1, lines2])
        plot.add_scene(scene)
        case_points = (points_list5_a, points_list5_b)
        case_polygon = (polygon5_a, polygon5_b)

    else:  # inside
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
        points_list6_a = [A, B, C, D, E]
        polygon6_a = [l1, l2, l3, l3, l4, l5]
        points1 = PointsCollection(points_list6_a, color="blue")
        lines1 = LinesCollection(polygon6_a, color='green')

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
        points_list6_b = [a, b, c, d, e]
        polygon6_b = [l1, l2, l3, l3, l4, l5]
        points2 = PointsCollection(points_list6_b, color="orange")
        lines2 = LinesCollection(polygon6_b, color='red')

        scene = Scene([points1, points2], [lines1, lines2])
        plot.add_scene(scene)
        case_points = (points_list6_a, points_list6_b)
        case_polygon = (polygon6_a, polygon6_b)

    plot.draw()
    return case_points, case_polygon


def main():
    case = int(sys.argv[1])
    case_points, case_polygons = initialize_polygons(case)
    InsidePolygon.check(case_points, case_polygons)


if __name__ == '__main__':
    main()
