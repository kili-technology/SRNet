import sys
from PIL import Image, ImageDraw, ImageFont
from matplotlib.font_manager import FontManager


if __name__ == "__main__":

    filename_source = sys.argv[1]
    image_input = Image.open(filename_source + ".jpg")

    image_input.save(filename_source + "_i_s.png", format="png")

    target_text = sys.argv[2]

    # only works for 1 line text
    w, h = (image_input.width, image_input.height) # imposed by input bounding box
    print(f"Original image size: {w}, {h}")
    m = 5 # margin in pixels
    fm = FontManager()
    ff = fm.findfont("arial")
    font_size = min(int(h / 4 * 3), int( ((w - 2 * m) / (len(target_text) * 0.5))))  # 22.5

    print(f"Computed font size: {font_size}")

    x, y = 3, 3
    img = Image.new('RGB', (w, h), color = (126, 126, 126))
    fnt = ImageFont.truetype(ff, font_size)
    d = ImageDraw.Draw(img)
    d.text((x,y), target_text, font=fnt, fill=(0,0,0))

    img.save(filename_source + "_i_t.png", format="png")


# pixel_per_character = 10
# n_lines = 1  -> for later
# split_target_text = target_text
# if pixel_per_character * len(target_text) > 120:
#     n_lines += 1
#     font_size = int(h/4 * 3 / n_lines)
#     split_target_text = "\n"
