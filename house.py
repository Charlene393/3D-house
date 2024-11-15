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
context.set_line_width(5)
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
context.set_line_width(5)
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
context.set_line_width(5)
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
context.set_line_width(5)
context.stroke_preserve()

set_rgb_color(context, 216, 165, 141)  # Fill color
context.fill()

# Draw a small circle
context.arc(540, 300, 5, 0, 2 * 3.14159)  # x=500, y=300, radius=10
context.set_source_rgb(1, 1, 0)  # Fill color: yellow
context.fill_preserve()
context.set_source_rgb(0, 0, 0)  # Stroke color: black
context.stroke()
# Draw windows
def draw_double_pane_window(ctx, x, y, width=40, height=80, is_side=False):
    """
    Draw a double-pane window with green frame and light blue glass
    Parameters:
        ctx: Cairo context
        x, y: Position coordinates
        width: Window width (default 40)
        height: Window height (default 80)
        is_side: Boolean to indicate if it's a side window (darker shading)
    """
    # Colors
    frame_color = (0.2, 0.6, 0.4)  # Green frame
    window_color = (0.8, 1, 1)  # Light blue glass

    # Frame thickness
    frame_thickness = 3

    # Draw outer frame
    ctx.rectangle(x, y, width, height)
    ctx.set_source_rgb(*frame_color)
    ctx.fill()

    # Window panes with proper spacing
    pane_spacing = height / 2

    # Draw top pane
    ctx.rectangle(
        x + frame_thickness,
        y + frame_thickness,
        width - 2 * frame_thickness,
        (height / 2) - 1.5 * frame_thickness
    )
    ctx.set_source_rgb(*window_color)
    ctx.fill()

    # Draw bottom pane
    ctx.rectangle(
        x + frame_thickness,
        y + (height / 2) + 0.5 * frame_thickness,
        width - 2 * frame_thickness,
        (height / 2) - 1.5 * frame_thickness
    )
    ctx.set_source_rgb(*window_color)
    ctx.fill()

    # Draw frame outlines
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(1)

    # Outer frame outline
    ctx.rectangle(x, y, width, height)
    ctx.stroke()

    # Middle divider
    ctx.move_to(x, y + height / 2)
    ctx.line_to(x + width, y + height / 2)
    ctx.stroke()


def draw_square_window(ctx, x, y, size=80):
    """
    Draw a square window with green frame and light blue glass, divided into four panes
    Parameters:
        ctx: Cairo context
        x, y: Position coordinates
        size: Window size (width and height are equal)
    """
    # Colors
    frame_color = (0.2, 0.6, 0.4)  # Green frame
    window_color = (0.8, 1, 1)  # Light blue glass

    # Frame thickness
    frame_thickness = 3

    # Draw outer frame
    ctx.rectangle(x, y, size, size)
    ctx.set_source_rgb(*frame_color)
    ctx.fill()

    # Calculate pane size
    pane_size = (size - 3 * frame_thickness) / 2

    # Draw four panes
    for row in range(2):
        for col in range(2):
            ctx.rectangle(
                x + frame_thickness + (col * (pane_size + frame_thickness)),
                y + frame_thickness + (row * (pane_size + frame_thickness)),
                pane_size,
                pane_size
            )
            ctx.set_source_rgb(*window_color)
            ctx.fill()

    # Draw frame outlines
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(1)

    # Outer frame outline
    ctx.rectangle(x, y, size, size)
    ctx.stroke()

    # Vertical divider
    ctx.move_to(x + size / 2, y)
    ctx.line_to(x + size / 2, y + size)
    ctx.stroke()

    # Horizontal divider
    ctx.move_to(x, y + size / 2)
    ctx.line_to(x + size, y + size / 2)
    ctx.stroke()

# Draw the window
draw_double_pane_window(context, 320, 290)
draw_double_pane_window(context, 410, 270)
draw_square_window(context, 145, 245)

context.set_source_rgb(0,0,0)
context.move_to(300,130)
context.line_to(350,90)
context.line_to(400, 120)

context.set_line_width(3)
context.stroke()
#small roof
#context.set_source_rgb(0,0,0)
#context.move_to(310, 130)
#context.line_to(345, 170)
#context.line_to(400,150)
#context.line_to(380,130)
#context.set_line_width(3)
#context.stroke()


# Save the result to a file
surface.write_to_png("3d_house.png")
print("Drawing saved to output.png")