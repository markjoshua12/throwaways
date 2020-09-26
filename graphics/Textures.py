import arcade
import PIL

SHEET_WIDTH = 16
SHEET_HEIGHT = 16

SPRITESHEET = arcade.load_spritesheet("res/spritesheet.png",
	8, 8, SHEET_HEIGHT, SHEET_WIDTH * SHEET_HEIGHT)

SPRITESHEET_16 = arcade.load_spritesheet("res/spritesheet-16.png",
    16, 16, 8, 8 * 8)

CHARS = arcade.load_spritesheet("res/chars.png", 6, 8, 27, 27 * 3)
CHARS_BOLD = arcade.load_spritesheet("res/chars.png", 8, 8, 27, 27 * 3)

for sprite in SPRITESHEET:
    sprite._hit_box_algorithm = "None"

for sprite in SPRITESHEET_16:
    sprite._hit_box_algorithm = "None"

for char in CHARS:
    char._hit_box_algorithm = "None"

for char in CHARS_BOLD:
    char._hit_box_algorithm = "None"

def get_texture(x, y, mirrored=False):
    if x < 0 or y < 0 or x >= SHEET_WIDTH or y >= SHEET_HEIGHT:
        return
    tex = SPRITESHEET[x + y * SHEET_WIDTH]
    if mirrored:
        tex.image = PIL.ImageOps.mirror(tex.image)
    return tex

def get_texture_from_spritesheet(x, y, spritesheet, w, h, mirrored=False):
    if x < 0 or y < 0 or x >= w or y >= h:
        return
    tex = spritesheet[x + y * w]
    if mirrored:
        tex.image = PIL.ImageOps.mirror(tex.image)
    return tex
