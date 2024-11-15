import cairo

# Set up canvas dimensions
WIDTH, HEIGHT = 600, 400

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set background color (white)
context.set_source_rgb(1, 1, 1)  # White
context.paint()

# Draw the front wall (rectangle)
context.set_source_rgb(0.9, 0.7, 0.5)  # Light beige color for the front wall
context.rectangle(250, 150, 250, 150)  # (x, y, width, height)
context.fill()

# Draw the side wall with a slight 3D perspective
context.set_source_rgb(0.8, 0.6, 0.4)  # Slightly darker color for side wall
context.move_to(250, 150)  # Top-left of front wall
context.line_to(150, 100)  # Top-left corner of side wall
context.line_to(145, 200)  # Bottom-left corner of side wall
context.line_to(250, 300)  # Bottom-left of front wall
context.close_path()
context.fill()


# Draw the door on the front wall
context.set_source_rgb(0.4, 0.2, 0.1)  # Darker color for the door
context.rectangle(450, 220, 30, 75)  # Door positioned on the front wall
context.fill()

#dommer
context.set_source_rgb(0,0,0)
context.move_to(450,300)
context.line_to(450,220)
context.line_to(485,220)
context.line_to(489,300)

context.set_line_width(3)
context.stroke()

#house line
context.set_source_rgba(0,0,0)
context.move_to(500, 150)
context.line_to(500, 300)
context.line_to(485,300)
context.line_to(480,292)
context.line_to(450,293)
context.line_to(450,300)
context.line_to(250,300)
context.line_to(150,200)
context.line_to(148,199)
context.line_to(150,100)
context.set_line_width(3)
context.stroke()


# Draw windows
def draw_window(context, x, y, width=40, height=80):
    # Colors
    frame_color = (0.2, 0.6, 0.4)  # Green frame
    window_color = (0.8, 1, 1)  # Light blue glass

    # Draw outer frame
    context.rectangle(x, y, width, height)
    context.set_source_rgb(*frame_color)
    context.fill()

    # Frame thickness
    frame_thickness = 4

    # Draw top pane
    context.rectangle(
        x + frame_thickness,
        y + frame_thickness,
        width - 2 * frame_thickness,
        (height - 3 * frame_thickness) / 2
    )
    context.set_source_rgb(*window_color)
    context.fill()

    # Draw bottom pane
    context.rectangle(
        x + frame_thickness,
        y + height / 2 + frame_thickness / 2,
        width - 2 * frame_thickness,
        (height - 3 * frame_thickness) / 2
    )
    context.set_source_rgb(*window_color)
    context.fill()

    # Add frame outlines for definition
    context.set_source_rgb(0, 0, 0)
    context.set_line_width(1)

    # Outer frame
    context.rectangle(x, y, width, height)
    context.stroke()

    # Middle divider
    context.move_to(x, y + height / 2)
    context.line_to(x + width, y + height / 2)
    context.stroke()


# Draw the window
draw_window(context, 350, 170)
draw_window(context, 300, 175)

# Save the result to an image file
surface.write_to_png("house_correct_orientation.png")
