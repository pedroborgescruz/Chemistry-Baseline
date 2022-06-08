"""
This program analyzes a set of chemistry data.
Author: Pedro Cruz
December 3rd, 2021
"""
from curve import *
import random

def print_choices():
    """
    This function prints the program's menu to the user.
    Parameters: None.
    Side-effects: Options printed to the user
    Return: None.
    """
    to_print = "Please select one of the following choices:\n"
    to_print += "(1) Graph Curve\n"
    to_print += "(2) Graph Baseline\n"
    to_print += "(3) Compute Peak Areas\n"
    to_print += "(4) Graph Several Curves\n"
    to_print += "(5) Quit"

    print(to_print)

def load_files():
    """
    Purpose: This function loads the file containing the dataset.
    Side effect: Generate a list of lists of the dataset.
    Parameters: None.
    Return: None.
    """
    curves = []
    file = open("/usr/local/doc/chemdata/large.tsv", "r")
    first_line = True

    for line in file:
        if first_line:
            points = line.strip().split(" ")
            n = points[0]
            m = points[1]

            for i in range(int(n)):
                new_curve = Curve()
                curves.append(new_curve)

            first_line = False

        else:
            points = line.strip().split("\t")

            for j in range(int(n)):
                x = float(points[0])
                y = float(points[j+1])

                curves[j].add_point(x, y)

    file.close()
    return curves

#opt 1
def graph_curve(curves):
    """
    Purpose: This function creates a graph of a curve selected by the user.
    Parameters: A list of curve objects.
    Side effect: Draws a user-selected curver on a window.
    Return: None.
    """
    choice = int(input("Which curve? "))

    while (int(choice) > len(curves)) or (int(choice) < 0):
        valid_range = len(curves) - 1
        print("Sorry, that choice is not valid.\nPick a number between 0 and "+
        "%d." %(valid_range))
        choice = input("Which curve? ")

    win = GraphWin("Curve Graph", 1000, 1000)

    xmin = curves[choice].get_min_x()
    xmax = curves[choice].get_max_x()
    ymin = curves[choice].get_min_y()
    ymax = curves[choice].get_max_y()
    win.setCoords(xmin,1.2*ymin,xmax,1.2*ymax)

    curves[int(choice)].draw(win)
    win.getMouse()
    win.close()

#opt 2
def graph_baseline(curves):
    """
    Purpose: This function generates the baseline of a user-selected curve.
    Parameters: A list of curve objects.
    Return: None.
    Side effects: Draws the user-chosen curve and its baseline.
    """

    choice = int(input("Which curve? "))

    while (int(choice) > len(curves)) or (int(choice) < 0):
        valid_range = len(curves) - 1
        print("Sorry, that choice is not valid.\nPick a number between 0 and " +
        "%d." %(valid_range))
        choice = input("Which curve? ")

    win = GraphWin("Curve Graph", 1000, 1000)

    xmin = curves[choice].get_min_x()
    xmax = curves[choice].get_max_x()
    ymin = curves[choice].get_min_y()
    ymax = curves[choice].get_max_y()
    win.setCoords(xmin,1.2*ymin,xmax,1.2*ymax)

    curves[choice].set_color("blue")
    baseline = curves[choice].get_baseline()
    baseline.set_color("red")
    curves[choice].draw(win)
    baseline.draw(win)
    win.getMouse()
    win.close()

def return_area(curve, y_baseline, baseline):
    """
    Purpose: This auxiliary function computes the total area bounded by a curve
        and its baseline through Riemann Sums.
    Parameters: curve - a curve object - and y_baseline - the y value of the
        baseline curve.
    Return: total_area - the sum of all the areas of the rectangles bounded by
        the curve and the baseline.
    Side effects: None.
    """
    area_list = []
    total_area = 0

    for i in range(1, curve.get_num_points()):
        width = abs(float(curve.get_point(i).getX()) -
        float(baseline.get_point(i-1).getX()))
        height = abs(float(curve.get_point(i).getY()) - float(y_baseline))
        area = (width * height)
        area_list.append(area)

    for value in area_list:
        total_area += value

    return total_area

#opt 3
def compute_area(curves):
    """
    Purpose: This function computes the total area bounded by a curve and its
        baseline through Riemann Sums.
    Parameters: A list of curve objects.
    Return: None.
    Side effects: None.
    """
    for i in range(len(curves)):
        baseline = curves[i].get_baseline()
        y_baseline = baseline.get_max_y()
        curve_area = return_area(curves[i], y_baseline, baseline)
        print("Area of curve %d: %.15f" %(i+1, curve_area))

    print()

#opt 4
def graph_curves(curves):
    """
    Purpose: This function creates a graph of multiple curves selected by the
        user.
    Parameters: A list of curve objects.
    Return: None.
    """
    colors = ["red", "blue", "yellow", "pink", "purple", "green", "cyan"]
    to_graph = []
    num = int(input("How many curves? "))

    while (num > len(curves)) or (num < 0):
        print("Sorry, that's out of range. Try again!")
        num = int(input("How many curves? "))

    for i in range(num):
        curve = int(input("Curve: "))

        while (curve > len(curves)) or (curve < 0):
            print("Sorry, that's out of range. Try again!")
            curve = int(input("Curve: "))

        to_graph.append(curves[curve])

    print()
    win = GraphWin("Curve Graph", 1000, 1000)

    xmin = to_graph[0].get_min_x()
    xmax = to_graph[0].get_max_x()
    ymin = to_graph[0].get_min_y()
    ymax = to_graph[0].get_max_y()
    win.setCoords(xmin,1.2*ymin,xmax,1.2*ymax)

    for j in range(len(to_graph)):
        to_graph[j].set_color(random.choice(colors))
        to_graph[j].draw(win)

    win.getMouse()
    win.close()

def main():
    curves = load_files()
    keep_going = True

    while keep_going:
        print_choices()
        print()
        choice = int(input("Choice? "))

        while choice not in [1, 2, 3, 4, 5]:
            print("I'm sorry, that's not a valid option. Try again!")
            choice = int(input("Choice? "))

        if (choice == 1):
            graph_curve(curves)
        elif (choice == 2):
            graph_baseline(curves)
        elif (choice == 3):
            compute_area(curves)
        elif (choice ==4):
            graph_curves(curves)
        else:
            keep_going = False
    quit()

main()
