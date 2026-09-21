import turtle
import math

# ============================================================
#  GANESHA - TURTLE ART
#  Inspired by the supplied reference image
#  Standard Python turtle only
# ============================================================

screen = turtle.Screen()
screen.setup(1100, 1100)
screen.bgcolor("#030303")
screen.title("Lord Ganesha - Turtle Art")
screen.colormode(255)

# Draw off-screen, then flip to the window in one go.
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# ------------------------------------------------------------
# BASIC DRAWING FUNCTIONS
# ------------------------------------------------------------

# --- view transform: the artwork spans roughly y = -540 .. +680, which is
# --- taller than the 1100px window, so scale it down slightly and recentre.
VIEW_SCALE = 0.80
VIEW_DY = -35

def V(p):
    """Map artwork coordinates to screen coordinates."""
    return (p[0] * VIEW_SCALE, p[1] * VIEW_SCALE + VIEW_DY)

def W(width):
    return max(1, width * VIEW_SCALE)

def goto(x, y):
    t.penup()
    t.goto(V((x, y)))

def polygon(points, fill, outline=None, width=1):
    t.penup()
    t.goto(V(points[0]))
    t.pendown()

    t.fillcolor(fill)
    t.pencolor(outline if outline else fill)
    t.pensize(W(width))

    t.begin_fill()
    for p in points[1:]:
        t.goto(V(p))
    t.goto(V(points[0]))
    t.end_fill()
    t.penup()

def ellipse(cx, cy, rx, ry, fill, outline=None, width=1,
            start=0, end=360, steps=80):
    """Draw a filled ellipse using a polygon."""
    points = []

    for i in range(steps + 1):
        a = math.radians(start + (end-start) * i/steps)
        x = cx + rx * math.cos(a)
        y = cy + ry * math.sin(a)
        points.append((x, y))

    polygon(points, fill, outline, width)

def arc(cx, cy, rx, ry, color, width=1,
        start=0, end=360, steps=80):
    """Unfilled elliptical arc / ring. Use instead of an empty fill color."""
    points = []

    for i in range(steps + 1):
        a = math.radians(start + (end-start) * i/steps)
        points.append((cx + rx*math.cos(a), cy + ry*math.sin(a)))

    line(points, color, width)

def circle(cx, cy, r, fill, outline=None, width=1):
    ellipse(cx, cy, r, r, fill, outline, width)

def line(points, color, width=2):
    t.penup()
    t.goto(V(points[0]))
    t.pendown()
    t.pencolor(color)
    t.pensize(W(width))

    for p in points[1:]:
        t.goto(V(p))

    t.penup()

def bezier(points, color, width=2, steps=40):
    """
    Draw a smooth Bezier curve.
    Works for 4 control points.
    """
    t.penup()
    t.goto(V(points[0]))
    t.pendown()
    t.pencolor(color)
    t.pensize(W(width))

    p0, p1, p2, p3 = points

    for i in range(steps + 1):
        u = i / steps
        x = (
            (1-u)**3*p0[0]
            + 3*(1-u)**2*u*p1[0]
            + 3*(1-u)*u**2*p2[0]
            + u**3*p3[0]
        )
        y = (
            (1-u)**3*p0[1]
            + 3*(1-u)**2*u*p1[1]
            + 3*(1-u)*u**2*p2[1]
            + u**3*p3[1]
        )
        t.goto(V((x, y)))

    t.penup()

def text(x, y, value, size, color, font="Arial", align="center"):
    goto(x, y)
    t.color(color)
    t.write(value, align=align,
            font=(font, max(6, int(size * VIEW_SCALE)), "bold"))

# ------------------------------------------------------------
# COLORS
# ------------------------------------------------------------

BLACK = "#030303"
DARK = "#120704"

GOLD_DARK = "#6e3505"
GOLD = "#c97808"
GOLD2 = "#e89a16"
GOLD_LIGHT = "#ffd05a"
GOLD_HI = "#ffe6a0"

RED = "#8c0715"
RED2 = "#b31324"
CRIMSON = "#650511"

ORANGE = "#ed7a0b"
ORANGE2 = "#ff9d16"
YELLOW = "#ffbd28"

SKIN = "#d87532"
SKIN2 = "#ef934e"
SKIN_LIGHT = "#ffb36b"
SKIN_HI = "#ffd095"

PINK = "#ef806f"
PINK2 = "#ff9b88"

WHITE = "#fff4dc"
GREEN = "#227522"
GREEN2 = "#49a42f"

BROWN = "#43200f"
BROWN2 = "#713816"

BLUE = "#143f59"

# ------------------------------------------------------------
# BACKGROUND GLOW
# ------------------------------------------------------------

for r, c in [
    (450, "#080402"),
    (430, "#100703"),
    (410, "#170a03"),
    (390, "#1c0c03"),
]:
    circle(0, 60, r, c)

# ------------------------------------------------------------
# GOLDEN HALO / CROWN BACKPLATE
# ------------------------------------------------------------

circle(0, 390, 245, GOLD_DARK)
circle(0, 390, 230, "#9a5008")
circle(0, 390, 214, "#3b1c05")

for i in range(32):
    a = math.radians(i * 360 / 32)
    x1 = math.cos(a) * 220
    y1 = 390 + math.sin(a) * 220
    x2 = math.cos(a) * 252
    y2 = 390 + math.sin(a) * 252

    line([(x1, y1), (x2, y2)], GOLD2, 5)

for i in range(24):
    a = math.radians(i * 15)
    x = math.cos(a) * 228
    y = 390 + math.sin(a) * 228
    circle(x, y, 7, GOLD_LIGHT)

# ------------------------------------------------------------
# BACK CLOTH / LARGE RED SHAWL
# ------------------------------------------------------------

polygon([
    (-400, -300),
    (-340, 120),
    (-250, 190),
    (-190, -250),
    (-100, -430),
    (-400, -430)
], CRIMSON)

polygon([
    (400, -300),
    (340, 120),
    (250, 190),
    (190, -250),
    (100, -430),
    (400, -430)
], CRIMSON)

line([(-390,-300),(-335,90),(-270,170)], GOLD2, 8)
line([(390,-300),(335,90),(270,170)], GOLD2, 8)

# ------------------------------------------------------------
# THRONE
# ------------------------------------------------------------

ellipse(0, -395, 330, 80, "#40200c", GOLD_DARK, 8)
ellipse(0, -390, 305, 55, "#7a3b09", GOLD, 5)

for x in range(-260, 261, 65):
    circle(x, -410, 17, GOLD_DARK, GOLD2, 3)
    circle(x, -410, 8, GOLD_LIGHT)

# ------------------------------------------------------------
# LARGE EARS
# ------------------------------------------------------------

ellipse(-190, 250, 115, 145, PINK, GOLD_DARK, 5)
ellipse(-195, 250, 82, 115, PINK2)

ellipse(190, 250, 115, 145, PINK, GOLD_DARK, 5)
ellipse(195, 250, 82, 115, PINK2)

bezier([(-260,310),(-220,280),(-220,205),(-170,165)], "#cf554d", 7)
bezier([(260,310),(220,280),(220,205),(170,165)], "#cf554d", 7)

bezier([(-235,340),(-205,310),(-195,260),(-180,210)], "#ffb09b", 5)
bezier([(235,340),(205,310),(195,260),(180,210)], "#ffb09b", 5)

# ------------------------------------------------------------
# BODY
# ------------------------------------------------------------

ellipse(0, -20, 205, 260, SKIN, GOLD_DARK, 6)
ellipse(0, -45, 165, 210, SKIN2)

ellipse(0, -135, 150, 145, SKIN_LIGHT)
ellipse(0, -155, 105, 95, "#e98b45")

ellipse(0, 90, 120, 120, SKIN_HI)

# ------------------------------------------------------------
# FACE / HEAD
# ------------------------------------------------------------

ellipse(0, 305, 155, 190, SKIN2, GOLD_DARK, 5)
ellipse(0, 320, 130, 160, SKIN_LIGHT)

ellipse(-105, 300, 35, 90, "#c8662c")
ellipse(105, 300, 35, 90, "#c8662c")

ellipse(0, 400, 95, 65, SKIN_HI)

# ------------------------------------------------------------
# EYES
# ------------------------------------------------------------

ellipse(-55, 345, 40, 25, "#7d3718")
ellipse(55, 345, 40, 25, "#7d3718")

ellipse(-55, 347, 30, 17, "#fff0d4")
ellipse(55, 347, 30, 17, "#fff0d4")

ellipse(-53, 347, 12, 15, "#120905")
ellipse(53, 347, 12, 15, "#120905")

circle(-49, 352, 4, WHITE)
circle(57, 352, 4, WHITE)

bezier([(-94,390),(-65,410),(-40,405),(-25,392)], "#4d1c0b", 8)
bezier([(94,390),(65,410),(40,405),(25,392)], "#4d1c0b", 8)

# ------------------------------------------------------------
# FOREHEAD TILAK
# ------------------------------------------------------------

line([(-9,430),(-9,462)], "#e52d16", 7)
line([(9,430),(9,462)], "#e52d16", 7)
line([(-9,458),(0,475),(9,458)], "#e52d16", 7)
line([(0,428),(0,465)], "#e52d16", 5)

text(0, 385, "\u0950", 35, "#e23819", "Arial")

# ------------------------------------------------------------
# TRUNK
# ------------------------------------------------------------

bezier([
    (0, 315),
    (-5, 220),
    (15, 120),
    (75, 70)
], SKIN_LIGHT, 82)

bezier([
    (75,70),
    (125,20),
    (115,-5),
    (70,-35)
], SKIN_LIGHT, 82)

bezier([
    (8,305),
    (10,215),
    (35,125),
    (80,75)
], "#db7735", 25)

ellipse(70, -40, 43, 34, SKIN2)
ellipse(70, -43, 20, 17, "#a83f28")

for y in range(160, 265, 24):
    line([(5,y),(22,y+12)], "#d93119", 3)

bezier([
    (8,255),(18,220),(20,180),(33,145)
], "#e33319", 4)

# ------------------------------------------------------------
# TUSKS
# ------------------------------------------------------------

polygon([
    (-105, 215),
    (-135, 175),
    (-128, 150),
    (-95, 190)
], WHITE, "#cdb99b", 3)

polygon([
    (105, 215),
    (135, 175),
    (128, 150),
    (95, 190)
], WHITE, "#cdb99b", 3)

# ------------------------------------------------------------
# CROWN
# ------------------------------------------------------------

ellipse(0, 470, 155, 55, GOLD_DARK, GOLD_LIGHT, 5)
ellipse(0, 455, 145, 48, GOLD, GOLD_LIGHT, 4)

polygon([
    (-135,450),
    (-120,535),
    (-75,585),
    (0,615),
    (75,585),
    (120,535),
    (135,450),
    (90,470),
    (0,490),
    (-90,470)
], GOLD_DARK)

circle(0, 520, 35, RED2, GOLD_LIGHT, 6)
circle(0, 520, 17, "#ff3824")

polygon([
    (-45,575),
    (0,675),
    (45,575)
], GOLD)

polygon([
    (-24,600),
    (0,660),
    (24,600)
], GOLD_LIGHT)

for x in [-105,-70,-35,35,70,105]:
    circle(x, 525, 13, GOLD2, GOLD_LIGHT, 3)

for y in [485,505,545,565]:
    line([(-120,y),(0,y+20),(120,y)], GOLD_LIGHT, 3)

# ------------------------------------------------------------
# NECKLACES
# ------------------------------------------------------------

def necklace(y, width, beads, color):
    for i in range(beads):
        x = -width + (2*width*i/(beads-1))
        yy = y + 22 * (1 - (x/width)**2)
        circle(x, yy, 8, color, GOLD_LIGHT, 2)

necklace(120, 120, 13, GOLD2)
necklace(80, 135, 15, GOLD)
necklace(35, 145, 17, GOLD2)

circle(0, 50, 30, GOLD_DARK, GOLD_LIGHT, 4)
circle(0, 50, 16, RED2)

# ------------------------------------------------------------
# GARLANDS
# ------------------------------------------------------------

def flower(x, y, scale=1):
    for a in range(0,360,60):
        rad = math.radians(a)
        px = x + math.cos(rad)*13*scale
        py = y + math.sin(rad)*13*scale
        ellipse(px, py, 9*scale, 14*scale, RED2)

    circle(x, y, 6*scale, GOLD)

for i in range(8):
    y = 130 - i*55
    x = -125 + abs(i-3.5)*4
    flower(x, y, 0.9)
    circle(x+18, y-12, 7, GREEN)

for i in range(8):
    y = 130 - i*55
    x = 125 - abs(i-3.5)*4
    flower(x, y, 0.9)
    circle(x-18, y-12, 7, GREEN)

for side in [-1,1]:
    for i in range(10):
        y = 155 - i*45
        x = side*(65 + i*8)
        circle(x, y, 10, WHITE)
        circle(x+side*8, y-5, 8, "#fff9ea")

# ------------------------------------------------------------
# ARMS
# ------------------------------------------------------------

ellipse(-250, 30, 55, 170, SKIN2)
ellipse(-280, 135, 45, 100, SKIN_LIGHT)

ellipse(250, 30, 55, 170, SKIN2)
ellipse(280, 135, 45, 100, SKIN_LIGHT)

ellipse(-135, -30, 50, 140, SKIN2)
ellipse(-155, 40, 40, 85, SKIN_LIGHT)

ellipse(145, -30, 50, 140, SKIN2)
ellipse(160, 30, 40, 90, SKIN_LIGHT)

# ------------------------------------------------------------
# LEFT HAND - AXE
# ------------------------------------------------------------

ellipse(-300, 150, 42, 55, SKIN_LIGHT, "#9d4c25", 3)

for i in range(4):
    ellipse(-325+i*15, 175-i*3, 10, 30, SKIN_LIGHT)

line([(-305,165),(-315,270),(-325,355)], GOLD2, 13)
line([(-307,165),(-317,270),(-327,355)], GOLD_LIGHT, 4)

polygon([
    (-360,370),
    (-325,395),
    (-290,380),
    (-280,350),
    (-315,335),
    (-350,350)
], GOLD_DARK, GOLD_LIGHT, 5)

polygon([
    (-355,370),
    (-325,388),
    (-300,375),
    (-320,360)
], GOLD)

# ------------------------------------------------------------
# RIGHT HAND - NOOSE
# ------------------------------------------------------------

ellipse(300, 150, 42, 55, SKIN_LIGHT, "#9d4c25", 3)

for i in range(4):
    ellipse(280+i*14, 175-i*2, 10, 30, SKIN_LIGHT)

bezier([
    (310,180),
    (330,270),
    (340,340),
    (320,390)
], GOLD2, 13)

bezier([
    (310,180),
    (330,270),
    (340,340),
    (320,390)
], GOLD_LIGHT, 4)

# loop (outline only - no fill)
arc(320, 415, 32, 55, GOLD_LIGHT, 7)

# ------------------------------------------------------------
# BLESSING HAND
# ------------------------------------------------------------

ellipse(-150, -5, 45, 75, SKIN_LIGHT, "#9d4c25", 3)

text(-150, -20, "\u0950", 32, "#d93418")

for i, x in enumerate([-178,-160,-142,-124]):
    ellipse(x, 70, 11, 48, SKIN_LIGHT, "#9d4c25", 2)

# ------------------------------------------------------------
# RIGHT HAND WITH BOWL
# ------------------------------------------------------------

ellipse(160, -35, 48, 65, SKIN_LIGHT, "#9d4c25", 3)

ellipse(170, -70, 75, 30, GOLD_DARK, GOLD_LIGHT, 5)
ellipse(170, -62, 68, 22, "#b96809", GOLD_LIGHT, 3)

ellipse(170, -105, 42, 18, GOLD_DARK, GOLD2, 4)

for x,y in [
    (125,-35),(150,-45),(175,-35),(200,-45),(225,-30),
    (138,-10),(165,-8),(192,-12),(215,-5),
    (154,18),(182,17)
]:
    circle(x,y,22,ORANGE2,GOLD_LIGHT,3)
    circle(x-5,y+7,5,"#ffc047")

# ------------------------------------------------------------
# DHOTI / LOWER CLOTHING
# ------------------------------------------------------------

ellipse(-150, -300, 155, 115, ORANGE2, GOLD_DARK, 6)
ellipse(-165, -320, 125, 85, "#ff9c11")

ellipse(150, -300, 155, 115, ORANGE2, GOLD_DARK, 6)
ellipse(165, -320, 125, 85, "#ff9c11")

polygon([
    (-100,-230),
    (0,-170),
    (100,-230),
    (130,-430),
    (0,-460),
    (-130,-430)
], ORANGE)

for x in [-110,-75,-40,-5,30,65,100]:
    line([
        (x,-250),
        (x*1.15,-330),
        (x*1.2,-420)
    ], "#ffbd32", 6)

line([(-260,-320),(-210,-385),(-140,-430)], GOLD_LIGHT, 10)
line([(260,-320),(210,-385),(140,-430)], GOLD_LIGHT, 10)

line([(-270,-335),(-215,-395),(-145,-440)], RED2, 7)
line([(270,-335),(215,-395),(145,-440)], RED2, 7)

# ------------------------------------------------------------
# FEET
# ------------------------------------------------------------

ellipse(-45, -465, 65, 30, SKIN_LIGHT, "#9d4c25", 3)
ellipse(45, -465, 65, 30, SKIN_LIGHT, "#9d4c25", 3)

for x in [-75,-50,-25,25,50,75]:
    ellipse(x,-460,8,13,SKIN_HI)

for x in [-55,55]:
    ellipse(x,-430,65,12,GOLD_DARK,GOLD_LIGHT,4)

# ------------------------------------------------------------
# JEWELRY ON WRISTS
# ------------------------------------------------------------

for x,y in [(-300,100),(300,100),(-150,-85),(165,-90)]:
    for r in [22,30,38]:
        ellipse(x,y,r,7,GOLD_DARK,GOLD_LIGHT,3)

# ------------------------------------------------------------
# MOUSE
# ------------------------------------------------------------

ellipse(335, -420, 75, 45, "#29251f", GOLD_DARK, 3)

ellipse(395, -390, 45, 42, "#342d26")

circle(385,-350,25,"#3d3028",GOLD_DARK,2)
circle(420,-350,23,"#3d3028",GOLD_DARK,2)

circle(385,-350,13,"#a85a50")
circle(420,-350,12,"#a85a50")

circle(408,-398,6,"#050505")
circle(410,-396,2,WHITE)

circle(432,-397,7,"#160a08")

ellipse(360,-450,20,12,"#44352c")
ellipse(400,-450,20,12,"#44352c")

bezier([
    (280,-420),
    (210,-470),
    (220,-515),
    (290,-510)
], "#4a3327", 9)

# mouse necklace (outline only - no fill)
arc(395, -405, 39, 45, GOLD_LIGHT, 5, start=200, end=330)

# ------------------------------------------------------------
# DIYA / OIL LAMP
# ------------------------------------------------------------

ellipse(-420,-445,60,20,GOLD_DARK,GOLD_LIGHT,4)
ellipse(-420,-438,45,13,GOLD,GOLD_LIGHT,3)

for r,c in [
    (40,"#3d1703"),
    (30,"#692805"),
    (20,"#a94b05")
]:
    circle(-420,-395,r,c)

polygon([
    (-420,-375),
    (-438,-405),
    (-430,-435),
    (-420,-415),
    (-408,-445),
    (-405,-410)
], "#ffae19")

polygon([
    (-420,-390),
    (-430,-412),
    (-420,-435),
    (-412,-410)
], "#fff19b")

# ------------------------------------------------------------
# BOOKS
# ------------------------------------------------------------

polygon([
    (-475,-485),
    (-290,-500),
    (-275,-460),
    (-465,-448)
], "#671018", GOLD_DARK, 4)

polygon([
    (-470,-450),
    (-285,-465),
    (-270,-435),
    (-460,-420)
], "#8d141b", GOLD_DARK, 4)

polygon([
    (-455,-445),
    (-300,-458),
    (-292,-445),
    (-450,-432)
], "#d4a25c")

text(-375,-475,"\u0965 \u0936\u094d\u0930\u0940 \u0917\u0923\u0947\u0936 \u0965",18,GOLD_LIGHT,"Arial")

# ------------------------------------------------------------
# LOTUS FLOWER
# ------------------------------------------------------------

for a in range(0,360,45):
    rad = math.radians(a)
    px = -110 + math.cos(rad)*35
    py = -495 + math.sin(rad)*20
    ellipse(px,py,28,14,"#e85b71")

ellipse(-110,-495,20,12,"#ff9a9f")
circle(-110,-495,7,GOLD)

# ------------------------------------------------------------
# EXTRA GOLD DECORATIONS
# ------------------------------------------------------------

for x in range(-180,181,30):
    circle(x,-95,8,GOLD2,GOLD_LIGHT,2)

ellipse(0,-220,160,22,GOLD_DARK,GOLD_LIGHT,5)

for x in range(-130,131,30):
    circle(x,-220,8,GOLD2)

circle(0,-220,25,GOLD_DARK,GOLD_LIGHT,4)
circle(0,-220,12,GREEN)

# ------------------------------------------------------------
# ORNAMENTAL JEWELS ON SHOULDERS
# ------------------------------------------------------------

for x in [-190,190]:
    circle(x,80,24,GOLD_DARK,GOLD_LIGHT,4)
    circle(x,80,12,RED2)

# ------------------------------------------------------------
# FOREHEAD / HEAD SMALL JEWELS
# ------------------------------------------------------------

for x,y,r in [
    (-80,430,8),
    (-45,455,7),
    (45,455,7),
    (80,430,8)
]:
    circle(x,y,r,RED2,GOLD_LIGHT,3)

# ------------------------------------------------------------
# SMALL GOLD SPARKLES
# ------------------------------------------------------------

sparkles = [
    (-315,400),(300,380),(-345,250),(345,250),
    (-260,470),(260,470),(-390,40),(390,40),
    (-250,-160),(260,-170)
]

for x,y in sparkles:
    line([(x-8,y),(x+8,y)],GOLD_LIGHT,2)
    line([(x,y-8),(x,y+8)],GOLD_LIGHT,2)

# ------------------------------------------------------------
# FINAL OUTLINE ACCENTS
# ------------------------------------------------------------

bezier([(-270,80),(-300,-10),(-300,-120),(-350,-240)],
        GOLD_DARK,8)

bezier([(270,80),(300,-10),(300,-120),(350,-240)],
        GOLD_DARK,8)

bezier([
    (-95,120),
    (-125,40),
    (-110,-40),
    (-75,-100)
], "#ffb76e", 8)

# ------------------------------------------------------------
# FINISH
# ------------------------------------------------------------

text(0,-535,"\u0950",22,GOLD_LIGHT)

screen.update()

turtle.done()