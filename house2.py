import cairo

# Define constants for the surface size
WIDTH, HEIGHT = 700, 500

# Helper function to set RGB colors using 0–255 values
def set_rgb_color(context, r, g, b):
    context.set_source_rgb(r / 255, g / 255, b / 255)

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_RGB30, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set the background color to white
context.set_source_rgb(1, 1, 1)  # White
context.paint()

# Draw the first polygon
context.move_to(100, 200)
context.line_to(100, 350)
context.line_to(270, 450)
context.line_to(272, 240)
context.line_to(200, 90)
context.close_path()

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(4)
context.stroke_preserve()

set_rgb_color(context, 216, 165, 141)  # Fill color
context.fill()

# Draw the second polygon
context.move_to(500, 370)
context.line_to(500, 250)
context.line_to(560, 230)
context.line_to(560, 350)

context.close_path()

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(4)
context.stroke_preserve()

set_rgb_color(context, 164, 106, 85)  # Fill color
context.fill()


# Draw the second polygon
context.move_to(270, 450)
context.line_to(500, 380)
context.line_to(500, 250)
context.line_to(560, 230)
context.line_to(560, 360)
context.line_to(600, 345)
context.line_to(600, 190)
context.line_to(272, 240)
context.close_path()

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(4)
context.stroke_preserve()

set_rgb_color(context, 255, 230, 202)  # Fill color
context.fill()

# Draw the third polygon
context.move_to(90, 210)
context.line_to(200, 90)
context.line_to(290, 270)
context.line_to(610, 190)
context.line_to(612, 180)
context.line_to(540, 40)
context.line_to(200, 80)
context.line_to(90, 200)
context.close_path()

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(4)
context.stroke_preserve()

set_rgb_color(context, 240, 93, 48)  # Fill color
context.fill()

# Draw the second polygon
context.move_to(560, 360)
context.line_to(552, 355)
context.line_to(550, 235)
context.line_to(558, 234)

context.close_path()

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(4)
context.stroke_preserve()

set_rgb_color(context, 216, 165, 141)  # Fill color
context.fill()

# Draw a small circle
context.arc(540, 300, 5, 0, 2 * 3.14159)  # x=500, y=300, radius=10
context.set_source_rgb(1, 1, 0)  # Fill color: yellow
context.fill_preserve()
context.set_source_rgb(0, 0, 0)  # Stroke color: black
context.stroke()



context.move_to(90, 200)
context.line_to(200, 80)
context.line_to(205, 78)
context.line_to(295, 260)
context.line_to(290, 270)
context.line_to(200, 90)
context.line_to(90, 210)

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(2)
context.stroke_preserve()

set_rgb_color(context, 185, 48, 17)  # Fill color
context.fill()

context.move_to(295, 260)
context.line_to(612, 182)
context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(2)
context.stroke_preserve()

#Window1
context.set_source_rgb(0.6, 0.9, 1.0)
context.move_to(300, 295)
context.line_to(350, 280)
context.line_to(350, 375)
context.line_to(300, 390)
context.close_path()
context.fill()

# Draw the lines inside front windows
context.set_source_rgb(0.1, 0.4, 0.3)
context.move_to(300, 342.5)
context.line_to(350, 327.5)
context.move_to(300, 295)
context.line_to(350, 280)
context.line_to(350, 375)
context.line_to(300, 390)
context.close_path()
context.set_line_width(3)
context.stroke()

#Window2
context.set_source_rgb(0.6, 0.9, 1.0)
context.move_to(400, 275)
context.line_to(450, 260)
context.line_to(450, 355)
context.line_to(400, 370)
context.close_path()
context.fill()

# Draw the lines inside front windows
context.set_source_rgb(0.1, 0.4, 0.3)
context.move_to(400, 320.5)
context.line_to(450, 305.5)
context.move_to(400, 275)
context.line_to(450, 260)
context.line_to(450, 355)
context.line_to(400, 370)
context.close_path()
context.set_line_width(3)
context.stroke()

# Save the result to a file
surface.write_to_png("output.png")
print("Drawing saved to output.png")