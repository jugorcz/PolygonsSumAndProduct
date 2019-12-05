from Plot import Plot
from Plot import LinesCollection
from Plot import PointsCollection
from Plot import Scene

from LinkedList import LinkedList
from BinarySearchTree import BinarySearchTree


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

        if start_point[0] > end_point[0]:
            start_point, end_point = end_point, start_point

        q.put(start_point[0], start_point[1])
        q.put(end_point[0], end_point[1])
        ok_line = (start_point, end_point)
        lines_dictionary[ok_line] = find_line_function(ok_line)
    return lines_dictionary, q


def get_line_starting_with(lines_dictionary, point):
    for line in lines_dictionary:
        if line[0] == point:
            return line
    return None


def get_line_ending_with(lines_dictionary, point):
    for line in lines_dictionary:
        if line[1] == point:
            return line
    return None


def is_point_on_list(points_list, point):
    found = False
    for p in points_list:
        if p == point:
            found = True
            break
    if found:
        points_list.remove(point)
        return True
    return False


def handle_line_begin_event(line, t):
    # insert line to T
    print(" start point")
    key = line
    value = line[0]
    t.put(key, value)


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


def handle_intersection_event(lines_dictionary, point, t, intersections_dictionary):
    print(" intersection point")
    first_line, second_line = find_two_intersecting_lines(lines_dictionary, point)
    if first_line and second_line:
        print("Intersection lines: ", end="")
        print(first_line, end="")
        print(" - ", end="")
        print(second_line)

        new_point = (round(point[0], 3), round(point[1], 3))
        intersections_dictionary[new_point] = (first_line, second_line)
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
    x = round(x, 5)
    y = (a1 * x) + b1
    y = round(y, 5)

    point = (x, y)

    if x < start_x:
        return None

    if is_point_on_line(point, line1) and is_point_on_line(point, line2):
        return point

    return None


def look_for_intersections(lines_dictionary, p, t, q, intersections_dictionary):
    for pair in t.generatePairs():
        line1 = pair[0]
        line2 = pair[1]
        start_x = p[0]
        print("Check pair: " + str(line1[0]) + "-" + str(line1[1]) + " and " + str(line2[0]) + "-" + str(line2[1]) + " at " + str(start_x))
        point = get_intersection_point(line1, line2, lines_dictionary, start_x)
        if point:
            print("------>Intersection! " + str(point))
            new_point = (round(point[0], 3), round(point[1], 3))
            if new_point not in intersections_dictionary:
                q.put(point[0], point[1])
                intersections_dictionary[new_point] = (line1, line2)


def is_start_point_checked(dictionary, point):
    for line in dictionary:
        if line[0] == point and dictionary[line] == False:
            dictionary[line] = True
            return line
    return None


def is_end_point_checked(dictionary, point):
    for line in dictionary:
        if line[1] == point and dictionary[line] == False:
            dictionary[line] = True
            return line
    return None


def check_if_intersects(lines_list):
    height = 10
    lines_dictionary, q = read_lines_list(lines_list)

    start_points_used_dictionary = dict()
    end_points_used_dictionary = dict()
    for line in lines_dictionary:
        start_points_used_dictionary[line] = False
        end_points_used_dictionary[line] = False

    lines_collection = LinesCollection(lines_list)
    my_scene = Scene([], [lines_collection])
    my_plot = Plot([my_scene])

    print("\n\nLines:")
    for line in lines_list:
        print(line)

    t = LinkedList(lines_dictionary)
    intersections_dictionary = dict()
    prev_point = None
    prev_line = None
    # Q: x->y
    while q.size > 0:
        event = q.findTheSmallest(q.root)
        point = (event.key, event.value)

        print("\n-------------------------------------------------\n" + str(point), end="")
        # update T
        begin_line = is_start_point_checked(start_points_used_dictionary, point)
        end_line = is_end_point_checked(end_points_used_dictionary, point)
        if begin_line is not None:
            handle_line_begin_event(begin_line, t)
            print("found line: " + str(begin_line))

        elif end_line is not None:
            handle_line_end_event(end_line, t)
            print("found line: " + str(end_line))

        else:  # intersection point
            handle_intersection_event(lines_dictionary, point, t, intersections_dictionary)

        # handle two line ends in the same point
        if prev_point == point:
            if end_line:
                print("Two ends intersection in: " + str(point))
                intersections_dictionary[point] = (prev_line, end_line)

        # update Q
        look_for_intersections(lines_dictionary, point, t, q, intersections_dictionary)

        q.delete(event.key, event.value)
        prev_line = end_line
        prev_point = point

    print("\nintersections number: " + str(len(intersections_dictionary)))
    for intersection in intersections_dictionary:
        point = intersection
        line1 = intersections_dictionary[intersection][0]
        line2 = intersections_dictionary[intersection][1]
        print(str(point) + " is intersection of " + str(line1) + " and " + str(line2))

        new_line = [(point[0], height - 1), (point[0], 1)]
        new_lines_collection = LinesCollection([new_line], color="red")
        points_collection = PointsCollection([point], color="green", marker="^")
        new_scene = Scene([points_collection], [lines_collection, new_lines_collection])
        my_plot.add_scene(new_scene)

    my_plot.draw()
    return intersections_dictionary


if __name__ == '__main__':
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

    a = (3, 2)
    b = (7, 3)
    c = (10, 2)
    d = (9, 5)
    e = (4, 4)
    l6 = [a, b]
    l7 = [b, c]
    l8 = [c, d]
    l9 = [d, e]
    l10 = [e, a]
    list5 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]

    check_if_intersects(list5)
