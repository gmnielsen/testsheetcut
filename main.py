import pygame as pg


class Spritecut:
    def __init__(self, filename, num_per_row, rows, wide, high, left_border = 0, top_border = 0, h_gap = 0, v_gap = 0):
        self.imagelist = []
        self.b_width = wide
        self.b_high = high
        self.image_count = num_per_row * rows
        # get the sheet of sprites
        self.sheet = pg.image.load(filename).convert_alpha()
        # loop through each row to get the images from that row
        for j in range (rows):
            for i in range (num_per_row):
                startx = left_border + (i * (self.b_width + h_gap))
                starty = top_border + (j * (self.b_high + v_gap))
                rect = pg.Rect(startx, starty, self.b_width, self.b_high)
                self.imagelist.append(self.get_sprite(rect))
    def get_sprite(self,rect):
        a_image = pg.Surface((self.b_width, self.b_high), pg.SRCALPHA).convert_alpha()
        a_image.blit(self.sheet,(0,0),rect)
        return a_image
    def show_sprite(self,number):
        return self.imagelist[number]

# global variables
appear_disappear = False
myindex = 0

# animation
def animate_images():
    global appear_disappear
    global myindex

    my_screen.blit(sheet.show_sprite(myindex), (160,160), (0, 0, sheet.b_width, sheet.b_high))

    if myindex == (sheet.image_count - 1) or myindex == 0:
        appear_disappear = not appear_disappear
    if appear_disappear:
        myindex += 1
    else:
        myindex -= 1

    pg.display.update()

# INITIALIZE GAME SCREEN
# initialization
SCRSIZE = (450,450)
pg.init()
# create the screen
my_screen = pg.display.set_mode(SCRSIZE)
color = (50,0,0)
my_screen.fill(color)
# create a clock for timing of screen flips
clock = pg.time.Clock()

# LOOP BOOLEAN
running = True
#Spritecut("filename", per row, rows, wide, high, left, top, h gap, v gap)
sheet = Spritecut("vapor_cloud.png", 5, 5, 128, 128, 5, 5)


while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    my_screen.fill(color)

    animate_images()

    # FLIP
    # flip() the display to put your work on screen
    pg.display.flip()

    # TIME
    # how often to update the screen
    # clock.tick(30)  # limits FPS to 30
    dt = clock.tick(5)

pg.quit()