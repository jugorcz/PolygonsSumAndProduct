from PolygonsSumAndProduct.Plot import Plot
from PolygonsSumAndProduct.Plot import LinesCollection
from PolygonsSumAndProduct.Plot import PointsCollection
from PolygonsSumAndProduct.Plot import Scene

from PolygonsSumAndProduct.LinkedList import LinkedList
from PolygonsSumAndProduct.BinarySearchTree import BinarySearchTree


def find_line_function(line):
    point1 = line[0]
    point2 = line[1]
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    a = (y1-y2)/(x1-x2)
    b = y1 - a*x1
    return a, b


def read_lines_list(lines_list):
    q = BinarySearchTree()
    lines_dictionary = dict()
    for line in lines_list:
        start_point = (line[0][0], line[0][1])
        end_point = (line[1][0], line[1][1])
        q.put(start_point[0], start_point[1])
        q.put(end_point[0], end_point[1])
        ok_line = (start_point, end_point)
        lines_dictionary[ok_line] = find_line_function(ok_line)
    return lines_dictionary, q


def get_line_from_dictionary(lines_dictionary, point):
    for line in lines_dictionary:
        if line[0] == point or line[1] == point:
            return line
    return None


def is_beginning_of_line(lines_dictionary, point):
    for line in lines_dictionary:
        if line[0] == point:
            return line
    return None


def handle_line_begin_event(line, t):
    # insert line to T
    print(" start point")
    key = line
    value = line[0]
    t.put(key, value)


def is_end_of_line(lines_dictionary, point):
    for line in lines_dictionary:
        if line[1] == point:
            return line
    return None


def handle_line_end_event(line, t):
    print(" end point")
    t.delete(line)


def calculate_function_value(x, function):
    a = function[0]
    b = function[1]
    y = a * x + b
    return round(y, 4)


def find_two_intersecting_lines(lines_dictionary, point):
    found_first_line = False
    first_line = None
    # print("\n start swap\n intersection point: " + str(point))
    for line in lines_dictionary:
        function = lines_dictionary[line]
        x = point[0]
        y = point[1]
        result = round(calculate_function_value(x, function), 4)
        # print("line :" + str(line[0]) + " = " + str(result))
        if round(result, 2) == round(y, 2):
            if found_first_line is False:
                first_line = line
                found_first_line = True
            else:
                second_line = line
                return first_line, second_line
    return None, None


def handle_intersection_event(lines_dictionary, point, t):
    print(" intersection point")
    first_line, second_line = find_two_intersecting_lines(lines_dictionary, point)
    if first_line and second_line:
        print("Intersection lines: ", end="")
        print(first_line, end="")
        print(" - ", end="")
        print(second_line)
        t.swapPlaces(first_line, second_line)
    else:
        print("Error: should be swap")


def is_point_on_line(point, line):
    x = point[0]
    y = point[1]

    x_min = line[0][0]
    x_max = line[1][0]
    if x_min > x_max:
        x_min, x_max = x_max, x_min

    y_min = line[0][1]
    y_max = line[1][1]
    if y_min > y_max:
        y_min, y_max = y_max, y_min

    if x < x_min or x > x_max:
        return False

    if y < y_min or y > y_max:
        return False

    return True


def get_intersection_point(line1, line2, dictionary, start_x):
    function1 = dictionary[line1]
    function2 = dictionary[line2]
    a1 = function1[0]
    b1 = function1[1]
    a2 = function2[0]
    b2 = function2[1]
    if a1 == a2:  # parallel lines
        return None
    x = (b2 - b1) / (a1 - a2)
    x = round(x, 4)
    y = (a1 * x) + b1
    y = round(y, 4)

    point = (x, y)
    # print(point)

    if x <= start_x:
        return None

    if is_point_on_line(point, line1) and is_point_on_line(point, line2):
        return point

    return None


def look_for_intersections(lines_dictionary, p, t, q, intersections_dictionary):
    for pair in t.generatePairs():
        line1 = pair[0]
        line2 = pair[1]
        start_x = p[0]
        print("Check pair: " + str(line1[0]) + " and " + str(line2[0]) + " at " + str(start_x))
        point = get_intersection_point(line1, line2, lines_dictionary, start_x)
        if point:
            print("------>Intersection! " + str(point))
            q.put(point[0], point[1])
            intersections_dictionary[point] = (line1, line2)


def check_if_intersects(lines_list):
    height = 10
    lines_dictionary, q = read_lines_list(lines_list)

    lines_collection = LinesCollection(lines_list)
    my_scene = Scene([], [lines_collection])
    my_plot = Plot([my_scene])
    # myPlot.draw()

    print("\n\nLines:\n")
    for line in lines_list:
        print(line)

    t = LinkedList(lines_dictionary)
    intersections_dictionary = dict()
    # Q: x->y
    while q.size > 0:
        event = q.findTheSmallest(q.root)
        point = (event.key, event.value)

        print("\n-------------------\n" + str(point), end="")
        # update T
        if is_beginning_of_line(lines_dictionary, point):
            line = get_line_from_dictionary(lines_dictionary, point)
            handle_line_begin_event(line, t)

        elif is_end_of_line(lines_dictionary, point):
            line = get_line_from_dictionary(lines_dictionary, point)
            handle_line_end_event(line, t)

        else:  # intersection point
            handle_intersection_event(lines_dictionary, point, t)

        # update Q
        look_for_intersections(lines_dictionary, point, t, q, intersections_dictionary)

        # display state
        new_line = [(point[0], height - 1), (point[0], 1)]
        print(new_line)
        new_lines_collection = LinesCollection([new_line], color="red")
        if point in intersections_dictionary:
            point_color = 'green'
        else:
            point_color = 'orange'

        points_collection = PointsCollection([point], color=point_color, marker="^")
        new_scene = Scene([points_collection], [lines_collection, new_lines_collection])
        my_plot.add_scene(new_scene)

        q.delete(event.key, event.value)

    my_plot.draw()

    print("intersections number: " + str(len(intersections_dictionary)))
    for intersection in intersections_dictionary:
        point = intersection
        line1 = intersections_dictionary[intersection][0]
        line2 = intersections_dictionary[intersection][1]
        print(str(point) + " is intersection of " + str(line1) + " and " + str(line2))


if __name__ == '__main__':
    check_if_intersects([])
