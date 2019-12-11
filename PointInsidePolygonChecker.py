import IntersectionsChecker as IC
from Plot import Scene
from Plot import LinesCollection
from Plot import PointsCollection
from Plot import Plot


def find_figure_range(figure_points):
    max_x = -1
    min_x = 100
    max_y = -1
    min_y = 100
    for point in figure_points:
        if point[0] > max_x:
            max_x = point[0]
        if point[0] < min_x:
            min_x = point[0]

        if point[1] > max_y:
            max_y = point[1]
        if point[1] < min_y:
            min_y = point[1]

    #print("x range: " + str(min_x) + "-" + str(max_x) + " y range: " + str(min_y) + ":" + str(max_y))
    return min_x, max_x, min_y, max_y


def make_line_from_point(point, max_x):
    end_point = (max_x+1, point[1])
    line = [point, end_point]
    return line


def is_point_on_list(points_list, point):
    for p in points_list:
        if point == p:
            return True
    return False


def is_outside(figure_points, figure, points_to_check):

    sum_points = []
    product_points = []

    min_x, max_x, min_y, max_y = find_figure_range(figure_points)
    for point in points_to_check:
        #print("\ncheck point: " + str(point))

        if is_point_on_list(figure_points, point): #common top
            #print("1 Inside")
            sum_points.append(point)
            product_points.append(point)
            continue

        if point[1] > max_y or point[1] < min_y or point[0] > max_x or point[0] < min_x:
            #print("1 Outside")
            sum_points.append(point)
            continue

        line = make_line_from_point(point, max_x)
        intersections_dictionary = IC.check_if_intersects(figure + [line], max_y)
        intersections_number = 0
        intersections_list = []

        for intersection in intersections_dictionary:
            if intersection[1] == point[1] and intersection[0] >= point[0]:
                #print(intersection)
                intersections_number += 1
                intersections_list.append(intersection)

        if intersections_number % 2 == 0:
            #print("2 Outside")
            sum_points.append(point)

        elif len(intersections_list) == 1:
            if is_point_on_list(figure_points, intersections_list[0]):
                p = intersections_list[0]

                if p[1] >= max_y or p[1] <= min_y or point[0] > p[0]:
                    #print("3 Outside")
                    sum_points.append(point)
                else:
                    #print("2 Inside")
                    product_points.append(point)
            else:
                #print("3 Inside")
                product_points.append(point)

    return sum_points, product_points


def find_figures_intersections(figure1, figure2, points1, points2, all_lines):
    intersections_dictionary = IC.check_if_intersects(figure1 + figure2, 12)
    points_list = []
    lines_list = []
    for intersection in intersections_dictionary:
        if is_point_on_list(points1, intersection) is False and is_point_on_list(points2, intersection) is False:
            points_list.append(intersection)
            line1 = intersections_dictionary[intersection][0]
            line2 = intersections_dictionary[intersection][1]
            if line1 not in lines_list:
                lines_list.append(line1)
            if line2 not in lines_list:
                lines_list.append(line2)

    for intersection in points_list:
        for line in intersections_dictionary[intersection]:
            line_to_delete = None
            for l in lines_list:
                if IC.is_point_on_line(intersection, l):
                    line_to_delete = l
                    delete_to_line = [l[1], l[0]]
                    break
            if line_to_delete in all_lines:
                all_lines.remove(line_to_delete)
            elif delete_to_line in all_lines:
                all_lines.remove(delete_to_line)

            lines_list.remove(line_to_delete)

            new_line1 = [line_to_delete[0], intersection]
            new_line2 = [intersection, line_to_delete[1]]
            lines_list.append(new_line1)
            lines_list.append(new_line2)
    all_lines += lines_list

    return points_list


def get_result_lines(lines_list, points):
    result_lines = []
    for line in lines_list:
        start = line[0]
        stop = line[1]
        found_start = False
        found_stop = False
        for point in points:
            if point == start:
                if found_stop:
                    result_lines.append(line)
                    break
                else:
                    found_start = True

            if point == stop:
                if found_start:
                    result_lines.append(line)
                    break
                else:
                    found_stop = True
    return result_lines


def check(case_points, case_polygons):

    figure1_points = case_points[0]
    figure2_points = case_points[1]

    figure1 = case_polygons[0]
    figure2 = case_polygons[1]

    sum_points, product_points = is_outside(figure2_points, figure2, figure1_points)
    sum, product = is_outside(figure1_points, figure1, figure2_points)
    sum_points += sum
    product_points += product

    all_lines = figure1 + figure2
    figure_intersections = find_figures_intersections(figure1, figure2, figure1_points, figure2_points, all_lines)

    sum_points += figure_intersections
    product_points += figure_intersections

    if len(product_points) == 0:
        print("Figures are separated")
        return

    sum_points_collection = PointsCollection(sum_points, color="blue")
    product_points_collection = PointsCollection(product_points, color="red")

    product_lines = get_result_lines(all_lines, product_points)
    product_lines_collection = LinesCollection(product_lines)

    sum_lines = get_result_lines(all_lines, sum_points)

    for line in product_lines:
        if line in sum_lines:
            sum_lines.remove(line)

    sum_lines_collection = LinesCollection(sum_lines, color = "green")

    scene1 = Scene([sum_points_collection], [sum_lines_collection])
    scene2 = Scene([product_points_collection], [product_lines_collection])
    plot = Plot([scene1])
    plot.add_scene(scene2)
    plot.draw()





