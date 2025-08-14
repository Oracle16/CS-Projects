# ===================================================================================
# file: goomba_theater.py
# author: Oracle16
# date: 04/22/2025
# ===================================================================================

from cs1graphics import *
from time import sleep
import math # Import math for the light animation

class Goomba(Layer):
    """
    Represents a Goomba enemy from Super Mario Bros as a cs1graphics Layer.

    This class creates a Goomba character using various polygon shapes.
    It allows for easy manipulation like moving, scaling, and rotating.
    You can also customize its colors and facial expression (mood).
    The reference point (for movement, rotation, scaling) is the
    bottom center point between the Goomba's shoes.
    """
    def __init__(self, face_color=(243,196,19), body_color=(234,208,2), shoe_color=(145,109,3), eye_color=(255,255,255), eyebrow_color=(170,131,2)):
        """
        Initializes a new Goomba instance.

        Args:
            face_color (tuple): RGB color for the main face/head.
            body_color (tuple): RGB color for the lower body section.
            shoe_color (tuple): RGB color for the shoes.
            eye_color (tuple): RGB color for the white part of the eyes (sclera).
            eyebrow_color (tuple): RGB color for the eyebrow.

        The Goomba is constructed from several Polygon shapes added to this Layer.
        The geometry is defined relative to the reference point (0,0), which
        represents the bottom-center of the Goomba.
        """
        Layer.__init__(self)
        # Store the colors used for potential later reference
        self._current_face_color = face_color
        self._current_body_color = body_color
        self._current_shoe_color = shoe_color
        self._current_eye_color = eye_color
        self._current_eyebrow_color = eyebrow_color

        # --- Define Goomba Body Parts ---

        # Face (main head shape)
        self.face_shape = Polygon(
            Point(0, -2), Point(0, 0), Point(-6, 0), Point(-9, -1), Point(-9, -8),
            Point(-6, -12), Point(-3, -15), Point(0, -18), Point(2, -21), Point(4, -23),
            Point(9, -23), Point(11, -21), Point(13, -18), Point(16, -15), Point(19, -12),
            Point(22, -8), Point(22, -1), Point(19, 0), Point(13, 0), Point(13, -2)
        )
        self.face_shape.setFillColor(face_color)
        self.face_shape.setBorderColor((243,196,1)) # Slightly darker border for definition
        self.add(self.face_shape)

        # Left Eye (white part)
        self.left_eye_sclera = Polygon(
            Point(0, -11), Point(-1, -11), Point(-1, -4), Point(4, -4),
            Point(4, -7), Point(3, -7), Point(3, -5), Point(0, -5)
        )
        self.left_eye_sclera.setFillColor(eye_color)
        self.left_eye_sclera.setBorderColor(eye_color) # No border for the white part
        self.add(self.left_eye_sclera)

        # Right Eye (white part)
        self.right_eye_sclera = Polygon(
            Point(14, -11), Point(13, -11), Point(13, -5), Point(10, -5),
            Point(10, -7), Point(9, -7), Point(9, -4), Point(14, -4)
        )
        self.right_eye_sclera.setFillColor(eye_color)
        self.right_eye_sclera.setBorderColor(eye_color) # No border
        self.add(self.right_eye_sclera)

        # Eyebrow (single shape covering both eyes)
        self.eyebrow_shape = Polygon(
            Point(17, -13), Point(17, -12), Point(13, -12), Point(12, -11),
            Point(12, -6), Point(11, -6), Point(11, -8), Point(2, -8),
            Point(2, -6), Point(1, -6), Point(1, -11), Point(0, -12),
            Point(-4, -12), Point(-4, -13), Point(-1, -14), Point(3, -10),
            Point(10, -10), Point(13, -14)
        )
        self.eyebrow_shape.setFillColor(eyebrow_color)
        self.eyebrow_shape.setBorderColor(eyebrow_color) # No border
        self.add(self.eyebrow_shape)

        # Lower Body (torso area)
        self.lower_body_shape = Polygon(
            Point(1, -2), Point(-1, 0), Point(-1, 3), Point(3, 7),
            Point(5, 7), Point(5, 9), Point(8, 9), Point(8, 7),
            Point(11, 4), Point(14, 3), Point(14, 0), Point(12, -2)
        )
        self.lower_body_shape.setFillColor(body_color)
        self.lower_body_shape.setBorderColor(body_color) # No border
        self.add(self.lower_body_shape)

        # Left Shoe
        self.left_shoe_shape = Polygon(
            Point(-1, 3), Point(-3, 3), Point(-4, 4), Point(-4, 6),
            Point(-3, 7), Point(-1, 9), Point(4, 9), Point(4, 8), Point(3, 7)
        )
        self.left_shoe_shape.setFillColor(shoe_color)
        self.left_shoe_shape.setBorderColor(shoe_color) # No border
        self.add(self.left_shoe_shape)

        # Right Shoe
        self.right_shoe_shape = Polygon(
            Point(14, 3), Point(11, 4), Point(9, 6), Point(9, 9),
            Point(17, 9), Point(19, 7), Point(20, 7), Point(20, 5),
            Point(20, 4), Point(17, 2), Point(15, 2)
        )
        self.right_shoe_shape.setFillColor(shoe_color)
        self.right_shoe_shape.setBorderColor(shoe_color) # No border
        self.add(self.right_shoe_shape)

        # Initialize mouth (will be drawn by _draw_mouth)
        self.mouth_shape = None
        self._draw_mouth(0, -3, mood="neutral") # Start with a neutral expression

    def _draw_mouth(self, center_x, center_y, mood="neutral"):
        """Internal helper to draw or redraw the mouth based on mood."""
        # Remove the previous mouth shape if it exists
        if self.mouth_shape:
            self.remove(self.mouth_shape)

        # Create the new mouth shape based on the mood
        if mood == "happy":
            # Upward curving path for a smile
            self.mouth_shape = Path(Point(center_x+3, center_y), Point(center_x+7, center_y+2), Point(center_x+11, center_y))
            self.mouth_shape.setBorderColor("green") # Happy color
        elif mood == "sad":
            # Downward curving path for a frown
            self.mouth_shape = Path(Point(center_x+3, center_y+2), Point(center_x+7, center_y), Point(center_x+11, center_y+2))
            self.mouth_shape.setBorderColor("blue") # Sad color
        else: # Neutral mood
            # Straight line for a neutral expression
            self.mouth_shape = Path(Point(center_x+3, center_y+1), Point(center_x+11, center_y+1))
            self.mouth_shape.setBorderColor("black") # Neutral color

        self.mouth_shape.setBorderWidth(2) # Make the mouth line visible
        self.add(self.mouth_shape) # Add the new mouth to the Goomba layer

    def change_face_color(self, new_color):
        """
        Changes the fill color of the Goomba's face/head.

        Args:
            new_color (tuple or str): The new RGB color or color name.
        """
        self.face_shape.setFillColor(new_color)
        self._current_face_color = new_color

    def change_eye_color(self, new_color):
        """
        Changes the fill color of the Goomba's eye sclera (white part).

        Args:
            new_color (tuple or str): The new RGB color or color name.
        """
        self.left_eye_sclera.setFillColor(new_color)
        self.left_eye_sclera.setBorderColor(new_color) # Match border to fill
        self.right_eye_sclera.setFillColor(new_color)
        self.right_eye_sclera.setBorderColor(new_color) # Match border to fill
        self._current_eye_color = new_color

    def set_mood(self, new_mood):
        """
        Changes the Goomba's facial expression by redrawing the mouth.

        Args:
            new_mood (str): The desired mood ("happy", "sad", or "neutral").
        """
        self._draw_mouth(0, -3, new_mood) # Redraw mouth at its standard position

    def bow(self):
        """Animates the Goomba performing a short bow (rotating forward and back)."""
        rotation_angle = -3 # Angle for each step of the bow
        steps_per_direction = 8 # Number of steps down and then up
        delay_between_steps = 0.01 # Short pause for smooth animation

        # Bow down
        for _ in range(steps_per_direction):
            self.rotate(rotation_angle)
            sleep(delay_between_steps)
        # Return to upright
        for _ in range(steps_per_direction):
            self.rotate(-rotation_angle) # Rotate back up
            sleep(delay_between_steps)

    def move_smoothly(self, delta_x, delta_y, total_steps=20, step_delay=0.01):
        """
        Animates the Goomba moving smoothly over a distance.

        Args:
            delta_x (float): Total horizontal distance to move.
            delta_y (float): Total vertical distance to move.
            total_steps (int): Number of small steps for the movement.
            step_delay (float): Pause duration between each small step.
        """
        move_x_per_step = delta_x / total_steps
        move_y_per_step = delta_y / total_steps
        for _ in range(total_steps):
            self.move(move_x_per_step, move_y_per_step)
            sleep(step_delay)

# --- Stage Drawing Functions ---

def add_mario_block_patterns(target_layer, x_start, y_start):
    """
    Adds decorative Mario-style block patterns onto a given layer.

    These patterns resemble the details on bricks in Super Mario Bros.
    They are drawn using Path objects with offsets.

    Args:
        target_layer (Layer): The cs1graphics Layer to add the patterns to.
        x_start (float): The starting X coordinate for the patterns (usually the left edge of a plank).
        y_start (float): The starting Y coordinate for the patterns (usually the top edge of a plank).
    """
    shadow_color = (234, 187, 181) # Light brown/pink for shadow effect
    shadow_width = 1.5
    outline_color = 'black'
    outline_width = 1

    # Pattern 1: Top-left corner detail
    pattern1_points = [
        Point(2 + x_start, 2 + y_start), Point(14 + x_start, 2 + y_start),
        Point(14 + x_start, -3 + y_start), Point(8 + x_start, -3 + y_start),
        Point(8 + x_start, -5 + y_start), Point(4 + x_start, -5 + y_start),
        Point(4 + x_start, -7 + y_start), Point(0 + x_start, -7 + y_start)
    ]
    shadow_path_1 = Path(*pattern1_points) # Unpack points into Path constructor
    shadow_path_1.setBorderColor(shadow_color)
    shadow_path_1.setBorderWidth(shadow_width)
    target_layer.add(shadow_path_1)
    outline_path_1 = Path(*pattern1_points)
    outline_path_1.setBorderColor(outline_color)
    outline_path_1.setBorderWidth(outline_width)
    target_layer.add(outline_path_1)

    # Pattern 2: Right edge detail
    pattern2_points = [
        Point(14 + x_start, 0 + y_start), Point(16 + x_start, 0 + y_start),
        Point(16 + x_start, -2 + y_start), Point(17 + x_start, -2 + y_start),
        Point(17 + x_start, -5 + y_start), Point(18 + x_start, -5 + y_start),
        Point(18 + x_start, -24 + y_start)
    ]
    shadow_path_2 = Path(*pattern2_points)
    shadow_path_2.setBorderColor(shadow_color)
    shadow_path_2.setBorderWidth(shadow_width)
    target_layer.add(shadow_path_2)
    outline_path_2 = Path(*pattern2_points)
    outline_path_2.setBorderColor(outline_color)
    outline_path_2.setBorderWidth(outline_width)
    target_layer.add(outline_path_2)

    # Pattern 3: Bottom-right internal detail
    pattern3_points = [
        Point(30 + x_start, -22 + y_start), Point(30 + x_start, -13 + y_start),
        Point(22 + x_start, -13 + y_start), Point(22 + x_start, -16 + y_start)
    ]
    shadow_path_3 = Path(*pattern3_points)
    shadow_path_3.setBorderColor(shadow_color)
    shadow_path_3.setBorderWidth(shadow_width)
    target_layer.add(shadow_path_3)
    outline_path_3 = Path(*pattern3_points)
    outline_path_3.setBorderColor(outline_color)
    outline_path_3.setBorderWidth(outline_width)
    target_layer.add(outline_path_3)

    # Pattern 4: Bottom edge detail
    pattern4_points = [
        Point(30 + x_start, -12 + y_start), Point(30 + x_start, 4 + y_start),
        Point(29 + x_start, 4 + y_start), Point(29 + x_start, 6 + y_start),
        Point(18 + x_start, 6 + y_start), Point(18 + x_start, 8 + y_start)
    ]
    shadow_path_4 = Path(*pattern4_points)
    shadow_path_4.setBorderColor(shadow_color)
    shadow_path_4.setBorderWidth(shadow_width)
    target_layer.add(shadow_path_4)
    outline_path_4 = Path(*pattern4_points)
    outline_path_4.setBorderColor(outline_color)
    outline_path_4.setBorderWidth(outline_width)
    target_layer.add(outline_path_4)

def draw_theater_stage(canvas, stage_width, stage_height):
    """
    Draws a complete theater stage scene onto the canvas.

    Includes background, curtains, overhead lights, and a decorated wooden floor.
    The curtains and floor are created as separate Layers.

    Args:
        canvas (Canvas): The main cs1graphics canvas object.
        stage_width (int): The width of the stage area (and canvas).
        stage_height (int): The height of the stage area (and canvas).

    Returns:
        Layer: The Layer object containing the curtain elements, allowing it
               to be animated independently (e.g., raised and lowered).
    """
    canvas.clear() # Ensure a fresh canvas
    # Set a deep blue background for a nighttime theater feel
    canvas.setBackgroundColor((30, 30, 60))

    # --- Create Curtains Layer ---
    curtain_layer = Layer()

    # Draw main red curtain folds using overlapping ellipses for a draped look
    fold_width = 44
    fold_height = 130
    fold_color = (180, 0, 0) # Deep red
    fold_border = (120, 0, 0) # Darker red border
    highlight_color = (255, 80, 80) # Lighter red for highlights
    highlight_width = 18
    highlight_height = 60
    for i in range(0, stage_width, 32): # Stride determines overlap
        fold_center_x = i
        fold_center_y = 70
        # Main fold shape
        fold = Ellipse(fold_width, fold_height, Point(fold_center_x, fold_center_y))
        fold.setFillColor(fold_color)
        fold.setBorderColor(fold_border)
        fold.setDepth(-90) # Behind highlights and trim
        curtain_layer.add(fold)
        # Highlight ellipse on top of the fold
        highlight = Ellipse(highlight_width, highlight_height, Point(fold_center_x, fold_center_y - 10)) # Slightly above center
        highlight.setFillColor(highlight_color)
        highlight.setBorderColor(highlight_color) # No border for highlight
        highlight.setDepth(-89) # In front of main fold
        curtain_layer.add(highlight)

    # Draw the top curtain valance (horizontal piece across the top)
    valance_height = 70
    valance_color = (220, 0, 0) # Slightly brighter red
    valance = Ellipse(stage_width + 40, valance_height, Point(stage_width // 2, 0)) # Wider than stage
    valance.setFillColor(valance_color)
    valance.setBorderColor(fold_border) # Use darker border
    valance.setDepth(-91) # Behind main folds
    curtain_layer.add(valance)

    # Add gold trim along the bottom edge of the valance
    gold_color = (255, 215, 0)
    dark_gold_color = (200, 160, 0)
    trim_y_position = 20
    gold_trim_line = Path(Point(0, trim_y_position), Point(stage_width, trim_y_position))
    gold_trim_line.setBorderColor(gold_color)
    gold_trim_line.setBorderWidth(8)
    gold_trim_line.setDepth(-90) # In front of valance, same level as folds
    curtain_layer.add(gold_trim_line)

    # Add hanging gold tassels from the trim
    tassel_top_y = 32
    tassel_bottom_y = 52
    tassel_ball_radius = 5
    tassel_ball_y = 54
    for i in range(32, stage_width, 64): # Spaced out tassels
        # Tassel line
        tassel_line = Path(Point(i, tassel_top_y), Point(i, tassel_bottom_y))
        tassel_line.setBorderColor(gold_color)
        tassel_line.setBorderWidth(4)
        tassel_line.setDepth(-89) # In front of folds
        curtain_layer.add(tassel_line)
        # Tassel ball at the bottom
        tassel_ball = Circle(tassel_ball_radius, Point(i, tassel_ball_y))
        tassel_ball.setFillColor(gold_color)
        tassel_ball.setBorderColor(dark_gold_color) # Darker gold border
        tassel_ball.setDepth(-88) # In front of tassel line
        curtain_layer.add(tassel_ball)

    # Add side curtain swags (decorative pieces at the sides)
    swag_width = 60
    swag_height = 160
    swag_y_center = 120
    left_swag = Ellipse(swag_width, swag_height, Point(0, swag_y_center))
    left_swag.setFillColor(fold_color)
    left_swag.setBorderColor(fold_border)
    left_swag.setDepth(-92) # Furthest back curtain element
    curtain_layer.add(left_swag)
    right_swag = Ellipse(swag_width, swag_height, Point(stage_width, swag_y_center))
    right_swag.setFillColor(fold_color)
    right_swag.setBorderColor(fold_border)
    right_swag.setDepth(-92)
    curtain_layer.add(right_swag)

    # Add the completed curtain layer to the main canvas
    canvas.add(curtain_layer)

    # --- Draw Overhead Stage Lights ---
    light_radius = 16
    light_y_position = 20
    light_color = (255, 255, 120) # Pale yellow
    light_border_color = (255, 255, 200) # Lighter yellow border
    num_lights = 5
    light_spacing = 100
    first_light_x = 60
    for i in range(num_lights):
        light_center_x = first_light_x + i * light_spacing
        overhead_light = Circle(light_radius, Point(light_center_x, light_y_position))
        overhead_light.setFillColor(light_color)
        overhead_light.setBorderColor(light_border_color)
        overhead_light.setDepth(-80) # In front of curtains
        canvas.add(overhead_light)

    # --- Create Decorated Wooden Floor Layer ---
    floor_layer = Layer()

    # Draw wooden floor planks (rectangles)
    plank_width = 32
    plank_height = 32
    plank_color = (255, 255, 255) # White planks for contrast with patterns
    plank_border_color = (0, 0, 0) # Black border
    floor_top_y = stage_height - plank_height
    for i in range(0, stage_width, plank_width):
        plank_center_x = i + plank_width / 2
        plank_center_y = floor_top_y + plank_height / 2
        plank = Rectangle(plank_width, plank_height, Point(plank_center_x, plank_center_y))
        plank.setFillColor(plank_color)
        plank.setBorderColor(plank_border_color)
        plank.setDepth(-70) # Behind footlights and trim
        floor_layer.add(plank)
        # Add the decorative block patterns onto each plank
        add_mario_block_patterns(floor_layer, x_start=i, y_start=floor_top_y)

    # Add gold trim along the top edge of the floor
    floor_trim_y = floor_top_y
    floor_trim_line = Path(Point(0, floor_trim_y), Point(stage_width, floor_trim_y))
    floor_trim_line.setBorderColor(gold_color)
    floor_trim_line.setBorderWidth(6)
    floor_trim_line.setDepth(-69) # In front of planks
    floor_layer.add(floor_trim_line)

    # Add footlights along the front edge of the stage floor
    footlight_radius = 8
    footlight_y_position = floor_trim_y - 4 # Slightly above the trim line
    footlight_color = "white"
    footlight_border_color = gold_color
    for i in range(0, stage_width, plank_width):
        footlight_center_x = i + plank_width / 2
        footlight_bulb = Circle(footlight_radius, Point(footlight_center_x, footlight_y_position))
        footlight_bulb.setFillColor(footlight_color)
        footlight_bulb.setBorderColor(footlight_border_color)
        footlight_bulb.setBorderWidth(2)
        footlight_bulb.setDepth(-60) # In front of floor trim
        floor_layer.add(footlight_bulb)

    # Add decorative plants in pots at the sides of the stage
    pot_color = (160, 82, 45) # Sienna brown
    pot_border_color = (110, 60, 30) # Darker brown
    stem_color = (34, 139, 34) # Forest green
    leaf_color = (50, 205, 50) # Lime green
    pot_width = 18
    pot_height = 12
    plant_y_base = floor_top_y + 4 # Base of the pot
    for plant_x_position in [32, stage_width - 32]: # Positions for left and right plants
        # Pot
        pot = Ellipse(pot_width, pot_height, Point(plant_x_position, plant_y_base))
        pot.setFillColor(pot_color)
        pot.setBorderColor(pot_border_color)
        pot.setDepth(-59) # In front of footlights
        floor_layer.add(pot)
        # Stem
        stem_bottom_y = plant_y_base - pot_height / 2
        stem_top_y = stem_bottom_y - 6
        stem = Path(Point(plant_x_position, stem_bottom_y), Point(plant_x_position, stem_top_y))
        stem.setBorderColor(stem_color)
        stem.setBorderWidth(4)
        stem.setDepth(-58) # In front of pot
        floor_layer.add(stem)
        # Leaves
        leaf_width = 10
        leaf_height = 6
        leaf_y_center = stem_top_y - 2
        leaf1 = Ellipse(leaf_width, leaf_height, Point(plant_x_position - 5, leaf_y_center))
        leaf1.setFillColor(leaf_color)
        leaf1.setBorderColor(stem_color) # Use stem color for border
        leaf1.setDepth(-57) # In front of stem
        floor_layer.add(leaf1)
        leaf2 = Ellipse(leaf_width, leaf_height, Point(plant_x_position + 5, leaf_y_center))
        leaf2.setFillColor(leaf_color)
        leaf2.setBorderColor(stem_color)
        leaf2.setDepth(-57)
        floor_layer.add(leaf2)

    # Add the completed floor layer to the main canvas
    canvas.add(floor_layer)

    # Return the curtain layer so it can be animated separately
    return curtain_layer

# --- Main Execution Block ---

if __name__ == '__main__':
    # Define canvas dimensions
    CANVAS_WIDTH = 512
    CANVAS_HEIGHT = 480

    # Create the main canvas window
    main_canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT, bgColor=(30, 30, 60), title='Goomba Theater!', autoRefresh=True)

    # Draw the stage elements and get a reference to the curtain layer
    the_curtain = draw_theater_stage(main_canvas, CANVAS_WIDTH, CANVAS_HEIGHT)

    # --- Create Goomba Actors ---
    # Define different Goomba variations
    goomba_actors = [
        Goomba(),  # Default classic Goomba
        Goomba(face_color=(200,76,12), eye_color=(244,180,165)),  # Brown face, pinkish eyes
        Goomba(face_color=(243,196,19), body_color=(200,76,12), shoe_color=(0,0,0)),  # Yellow face, brown body, black shoes
        Goomba(face_color=(243,196,19), eye_color="blue", eyebrow_color="black")  # Default face, blue eyes, black brows
    ]

    # Define starting positions for each Goomba on the stage floor
    actor_start_positions = [
        (120, CANVAS_HEIGHT - 40), # Adjusted Y for floor level
        (220, CANVAS_HEIGHT - 40),
        (320, CANVAS_HEIGHT - 40),
        (420, CANVAS_HEIGHT - 40)
    ]

    # Place each Goomba actor onto the canvas at its starting position
    for actor, start_pos in zip(goomba_actors, actor_start_positions):
        start_x, start_y = start_pos
        actor.moveTo(start_x, start_y)
        main_canvas.add(actor)

    # --- Animation Sequence ---

    # 1. Animate Overhead Lights: Orbit like mini-moons
    print("Animating overhead lights...")
    overhead_stage_lights = []
    # Find the Circle objects that represent the overhead lights
    for graphic_object in main_canvas.getContents():
        if isinstance(graphic_object, Circle) and graphic_object.getReferencePoint().getY() == 20 and graphic_object.getRadius() == 16:
            overhead_stage_lights.append(graphic_object)

    # Store the initial positions of the lights
    original_light_positions = [light.getReferencePoint() for light in overhead_stage_lights]

    # Define parameters for the orbit animation
    orbit_radius = 40       # How far the lights move from their center
    orbit_center_y = 60     # Vertical center of the orbit path
    orbit_animation_steps = 60 # Number of steps for the orbit motion

    # Animate lights moving up in a semi-circular path
    for orbit_step in range(orbit_animation_steps):
        # Calculate angle from 0 to pi (0 to 180 degrees)
        orbit_angle = math.pi * orbit_step / (orbit_animation_steps - 1)
        for light_index, current_light in enumerate(overhead_stage_lights):
            original_x = original_light_positions[light_index].getX()
            # Calculate new position using trigonometry for circular motion
            new_x = original_x + orbit_radius * math.cos(orbit_angle) # Moves horizontally
            new_y = orbit_center_y - orbit_radius * math.sin(orbit_angle) # Moves vertically (up then down)
            current_light.moveTo(new_x, new_y)
        sleep(0.01) # Short pause for smooth animation

    # Animate lights returning smoothly ("majestically") to original positions
    for orbit_step in range(orbit_animation_steps):
        # Interpolation factor: goes from 1 down to 0
        interpolation_factor = 1 - orbit_step / (orbit_animation_steps - 1)
        for light_index, current_light in enumerate(overhead_stage_lights):
            original_x, original_y = original_light_positions[light_index].getX(), original_light_positions[light_index].getY()
            # Calculate the position at the end of the upward orbit (angle = pi)
            end_orbit_x = original_x + orbit_radius * math.cos(math.pi)
            end_orbit_y = orbit_center_y - orbit_radius * math.sin(math.pi) # Should be orbit_center_y
            # Linearly interpolate between the end orbit position and the original position
            new_x = interpolation_factor * end_orbit_x + (1 - interpolation_factor) * original_x
            new_y = interpolation_factor * end_orbit_y + (1 - interpolation_factor) * original_y
            current_light.moveTo(new_x, new_y)
        sleep(0.01)
    print("Light animation complete.")

    # 2. Curtain Rises: Animate the curtain layer moving upwards
    print("Raising the curtain...")
    curtain_rise_steps = 60
    curtain_move_per_step = -2 # Move upwards
    for _ in range(curtain_rise_steps):
        the_curtain.move(0, curtain_move_per_step)
        sleep(0.01)
    print("Curtain raised.")

    # 3. Goombas Act: Perform various actions simultaneously or sequentially
    print("Goombas perform!")
    # Example actions: move and change mood
    goomba_actors[0].move_smoothly(0, -40) # Move up slightly
    goomba_actors[0].set_mood("happy")
    goomba_actors[1].move_smoothly(40, 0) # Move right slightly
    goomba_actors[1].set_mood("sad")
    goomba_actors[2].move_smoothly(-40, 0) # Move left slightly
    goomba_actors[2].set_mood("happy")
    goomba_actors[3].move_smoothly(0, -40) # Move up slightly
    goomba_actors[3].set_mood("sad")
    sleep(0.5) # Pause after actions

    # 4. All Goombas Take a Bow
    print("Goombas take a bow.")
    for goomba_actor in goomba_actors:
        goomba_actor.bow()
    sleep(0.5) # Pause after bowing

    # 5. Curtain Falls: Animate the curtain layer moving downwards
    print("Lowering the curtain...")
    for _ in range(curtain_rise_steps): # Use same number of steps to lower
        the_curtain.move(0, -curtain_move_per_step) # Move downwards
        sleep(0.01)
    print("Curtain lowered.")

    # 6. End Scene: Remove Goombas (optional fade-out effect)
    print("Show's over! Fading out...")
    sleep(0.5)
    for goomba_actor in goomba_actors:
        main_canvas.remove(goomba_actor)
    print("Scene clear.")

    # Keep the window open until manually closed
    # main_canvas.wait() # Uncomment if the window closes immediately