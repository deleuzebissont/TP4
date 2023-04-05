import arcade
import random

# je definis les dimensions de l ecran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# je definis les couleurs possibles et en choisi une au hasard
COLORS = [arcade.color.BLACK_BEAN, arcade.color.AFRICAN_VIOLET, arcade.color.ELECTRIC_YELLOW]
random.choice(COLORS)


class Cercle:
    def __init__(self, radius, centre_x, centre_y, color, change_x, change_y):
        # je definis les attributs de mon cercle comme son rayon, sa couleur, son changement en x (etc...)
        self.radius = radius
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.color = color
        self.change_x = change_x
        self.change_y = change_y

    # la methode va nous permettre de stocker le dessin du cercle
    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.radius, self.color)


class Rectangle:
    # je definis les attributs du rectangle tel que le centre_x (x), sa largeur, sa hauteur, son angle
    def __init__(self, centre_x, centre_y, change_x, change_y, width, height, color, angle):
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle
    # encore une fois, cette methode va nous permettre de stocker le dessin du retangle
    def draw(self):
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.width, self.height, self.color, self.angle)


class MyGame(arcade.Window):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "TP4")
        # nous creeons deux listes dans lesquelles il nous sera possible de stccker notre nombre de formes
        self.list_cercle = []
        self.list_rectangle = []

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        # cette methode appele la methode draw definit plus tot et dessinera ainsi les cercles de la list_cercle et
        # les rectangles de la list_rectangle
        for cercle in self.list_cercle:
            cercle.draw()
        for rectangle in self.list_rectangle:
            rectangle.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        # nous definissions ce qui sera dessine si nous appuyons sur un des deux boutons de la souris (nous donnons
        # des valeurs aleatoires concretes aux attributs des methodes des classes plus hautes)
        if button == arcade.MOUSE_BUTTON_LEFT:
            radius = random.randint(10, 30)
            center_x = x
            center_y = y
            color = random.choice(COLORS)
            change_x = random.randint(5, 20)
            change_y = random.randint(5, 20)
            cercle = Cercle(radius, center_x, center_y, color, change_x, change_y)
            self.list_cercle.append(cercle)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            width = random.randint(10, 50)
            height = random.randint(10, 50)
            angle = random.randint(0, 180)
            center_x = x
            center_y = y
            change_x = random.randint(5, 20)
            change_y = random.randint(5, 20)
            color = random.choice(COLORS)
            rectangle = Rectangle(center_x, center_y, change_x, change_y, width, height, color, angle)
            self.list_rectangle.append(rectangle)

    def update(self, delta_time: float):
        global cercle
        for cercle in self.list_cercle:
            # nous actualisons la position du cercle
            cercle.centre_x += cercle.change_x
            cercle.centre_y += cercle.change_y
            # si le cercle percute une des parois de l ecran, il est renvoye dans le sens oppose en faisant
            # tout simplement son changement en x et en y mais * -1
            if cercle.centre_x + cercle.radius > SCREEN_WIDTH or cercle.centre_x - cercle.radius < 0:
                cercle.change_x *= -1
            if cercle.centre_y + cercle.radius > SCREEN_HEIGHT or cercle.centre_y - cercle.radius < 0:
                cercle.change_y *= -1
        # nous actualisons la position du rectangle
        for rectangle in self.list_rectangle:
            rectangle.centre_x += rectangle.change_x
            rectangle.centre_y += rectangle.change_y
            # comme avec le cercle nous renvoyons le rectangle dans le sens oppose si celui ci percute une paroi
            if rectangle.centre_x + rectangle.width > SCREEN_WIDTH or rectangle.centre_x - rectangle.width < 0:
                rectangle.change_x *= -1
            if rectangle.centre_y + rectangle.height > SCREEN_HEIGHT or rectangle.centre_y - rectangle.height < 0:
                rectangle.change_y *= -1

# nous associons les dimensions du debut a l ecran puis nous executons l ensemble du code
def main():
    my_game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    my_game.setup()

    arcade.run()


main()
