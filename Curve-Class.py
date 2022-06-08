
from graphics import *

class Curve(object):
    def __init__(self):
        """
        Constructor: make a new curve.
        """
        self.points = []
        self.color = "black"

    def __str__(self):
        if self.points == []:
            to_return = "Number of points: %d\n" %(len(self.points))
            to_return += "Color: %s\n" %(self.color)
            to_return += "------\n"

        else:
            to_return = "Points:\n"
            for i in range(4):
                to_return += str(self.points[i]) + "\n"
            to_return += str(self.points[4])
            to_return += "\n...\n"
            to_return += "------"

        return to_return

    def add_point(self, x, y):
        point = Point(x, y)
        point.setFill(self.color)
        self.points.append(point)

    def set_color(self, color):
        self.color = color
        for i in range(len(self.points)):
            self.points[i].setFill(color)

    def get_num_points(self):
        return len(self.points)

    def get_point(self, i):
        return self.points[i]

    def get_min_x(self):
        for i in range(0, len(self.points)-1):
            min_x = i
            for j in range(1, len(self.points)):
                if self.points[min_x].getX() > self.points[j].getX():
                    min_x = j
            save = self.points[i]
            self.points[i] = self.points[min_x]
            self.points[min_x] = save

        return self.points[0].getX()

    def get_max_x(self):
        for i in range(0, len(self.points)-1):
            max_x = i
            for j in range(1, len(self.points)):
                if self.points[j].getX() > self.points[max_x].getX():
                    max_x = j
            save = self.points[i]
            self.points[i] = self.points[max_x]
            self.points[max_x] = save

        return self.points[0].getX()
        
    def get_min_y(self):
        for i in range(0, len(self.points)-1):
            min_y = i
            for j in range(1, len(self.points)):
                if self.points[min_y].getY() > self.points[j].getY():
                    min_y = j
            save = self.points[i]
            self.points[i] = self.points[min_y]
            self.points[min_y] = save

        return self.points[0].getY()

    def get_max_y(self):
        for i in range(0, len(self.points)-1):
            max_y = i
            for j in range(1, len(self.points)):
                if self.points[j].getY() > self.points[max_y].getY():
                    max_y = j
            save = self.points[i]
            self.points[i] = self.points[max_y]
            self.points[max_y] = save

        return self.points[0].getY()

    def draw(self, win):
        for i in range(len(self.points)):
            self.points[i].draw(win)

    def get_baseline(self):
        ymax = self.get_max_y()
        baseline = Curve()

        for i in range(len(self.points)):
            baseline.add_point(self.points[i].getX(), ymax)

        return baseline

def main():
  curve = Curve()
  print(curve)
  x=-5
  while x <= 5:
    curve.add_point(x, x**3 - 15*x)
    x += 0.05
  print(curve)
  curve.set_color("green")
  print(curve)

  win = GraphWin("Testing Curve class", 1000, 1000)
  xmin = curve.get_min_x()
  xmax = curve.get_max_x()
  ymin = curve.get_min_y()
  ymax = curve.get_max_y()
  print("%.2f, %.2f, %.2f, %.2f" % (xmin,ymin,xmax,ymax))
  win.setCoords(xmin,ymin,xmax,1.2*ymax)
  curve.draw(win)

  win.getMouse()
  baseline = curve.get_baseline()
  baseline.set_color("red")
  baseline.draw(win)

  win.getMouse()

if __name__ == "__main__":
  main()
