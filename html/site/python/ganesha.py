import os
import sys
import importlib


# Pygame is loaded dynamically so the script can start far enough to show a
# useful installation message when the selected Python environment lacks it.
try:
    pygame = importlib.import_module("pygame")
except ImportError:
    pygame = None


# NumPy is loaded dynamically for the same reason as OpenCV below: the
# editor may be using a different Python environment than the one running
# the script.
try:
    np = importlib.import_module("numpy")
except ImportError:
    np = None


# OpenCV is loaded dynamically so the script can start even when the
# editor's selected Python environment does not have the package installed.
try:
    cv2 = importlib.import_module("cv2")
except ImportError:
    cv2 = None


# =====================================================
# SETTINGS
# =====================================================

WIDTH = 650
HEIGHT = 850

FPS = 60
DRAW_TIME = 60

BLACK = (0, 0, 0)
GOLD = (255, 175, 35)
LIGHT_GOLD = (255, 225, 125)
DARK_GOLD = (95, 42, 5)


# =====================================================
# IMAGE PATH
# =====================================================

BASE_FOLDER = os.path.dirname(
    os.path.abspath(__file__)
)

IMAGE_PATH = os.path.join(
    BASE_FOLDER,
    "ganesh.png"
)


# =====================================================
# IMAGE LOAD
# =====================================================

def load_image():

    if np is None:

        print("ERROR: NumPy installed nahi hai!")
        print("Command prompt mein yeh command chalao:")
        print("python -m pip install numpy")
        input("Enter dabao...")
        sys.exit()

    if cv2 is None:

        print("ERROR: OpenCV installed nahi hai!")
        print("Command prompt mein yeh command chalao:")
        print("python -m pip install opencv-python")
        input("Enter dabao...")
        sys.exit()

    if not os.path.exists(IMAGE_PATH):

        print()
        print("ERROR: ganesh.png nahi mili!")
        print()
        print("Image yahan rakho:")
        print(IMAGE_PATH)
        print()

        input("Enter dabao...")
        sys.exit()

    image = cv2.imread(
        IMAGE_PATH,
        cv2.IMREAD_COLOR
    )

    if image is None:

        print("ERROR: Image open nahi ho rahi!")
        input("Enter dabao...")
        sys.exit()

    return image


# =====================================================
# RESIZE IMAGE
# =====================================================

def resize_image(image):

    image_height, image_width = image.shape[:2]

    scale = min(
        (WIDTH - 30) / image_width,
        (HEIGHT - 30) / image_height
    )

    new_width = int(image_width * scale)
    new_height = int(image_height * scale)

    resized = cv2.resize(
        image,
        (new_width, new_height),
        interpolation=cv2.INTER_AREA
    )

    canvas = np.zeros(
        (HEIGHT, WIDTH, 3),
        dtype=np.uint8
    )

    x = (WIDTH - new_width) // 2
    y = (HEIGHT - new_height) // 2

    canvas[
        y:y + new_height,
        x:x + new_width
    ] = resized

    return canvas


# =====================================================
# CREATE CLEAN OUTLINE
# =====================================================

def create_outline(image):

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Smooth noise
    gray = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    # Image ke edges detect
    edges = cv2.Canny(
        gray,
        35,
        110
    )

    # Bright subject ka outer shape
    foreground = cv2.threshold(
        gray,
        18,
        255,
        cv2.THRESH_BINARY
    )[1]

    kernel = np.ones(
        (3, 3),
        np.uint8
    )

    foreground = cv2.morphologyEx(
        foreground,
        cv2.MORPH_CLOSE,
        kernel
    )

    # Outer silhouette
    outer_contours, _ = cv2.findContours(
        foreground,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE
    )

    outer = np.zeros_like(
        foreground
    )

    for contour in outer_contours:

        if cv2.contourArea(contour) > 1000:

            cv2.drawContours(
                outer,
                [contour],
                -1,
                255,
                2
            )

    # Internal details + outer shape
    combined = cv2.bitwise_or(
        edges,
        outer
    )

    # Lines ko clean/thoda thick karna
    combined = cv2.dilate(
        combined,
        np.ones((2, 2), np.uint8),
        iterations=1
    )

    return combined


# =====================================================
# CONTOURS KO SMOOTH PATHS MEIN CONVERT KARNA
# =====================================================

def create_paths(outline):

    contours, _ = cv2.findContours(
        outline,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_NONE
    )

    paths = []

    for contour in contours:

        length = cv2.arcLength(
            contour,
            False
        )

        if length < 35:
            continue

        # Smooth contour
        epsilon = 1.2

        smooth_contour = cv2.approxPolyDP(
            contour,
            epsilon,
            False
        )

        points = []

        for point in smooth_contour:

            x, y = point[0]

            if (
                0 <= x < WIDTH
                and 0 <= y < HEIGHT
            ):

                points.append(
                    (int(x), int(y))
                )

        if len(points) >= 2:

            paths.append(points)

    # Pehle upper part, phir lower part
    paths.sort(
        key=lambda path: (
            min(point[1] for point in path),
            -len(path)
        )
    )

    return paths


# =====================================================
# PATH LENGTH
# =====================================================

def path_length(path):

    total = 0

    for i in range(
        1,
        len(path)
    ):

        x1, y1 = path[i - 1]
        x2, y2 = path[i]

        distance = (
            (x2 - x1) ** 2
            + (y2 - y1) ** 2
        ) ** 0.5

        total += distance

    return total


# =====================================================
# GLOWING LINE DRAW
# =====================================================

def draw_path(
    screen,
    path,
    progress
):

    if len(path) < 2:
        return

    progress = max(
        0,
        min(progress, 1)
    )

    visible_count = int(
        2 + (
            (len(path) - 2)
            * progress
        )
    )

    visible_count = min(
        visible_count,
        len(path)
    )

    visible_points = path[
        :visible_count
    ]

    if len(visible_points) < 2:
        return

    # Soft outer glow
    pygame.draw.lines(
        screen,
        DARK_GOLD,
        False,
        visible_points,
        10
    )

    # Middle glow
    pygame.draw.lines(
        screen,
        (190, 95, 12),
        False,
        visible_points,
        5
    )

    # Main golden line
    pygame.draw.lines(
        screen,
        GOLD,
        False,
        visible_points,
        3
    )

    # Bright centre line
    pygame.draw.lines(
        screen,
        LIGHT_GOLD,
        False,
        visible_points,
        1
    )


# =====================================================
# MAIN PROGRAM
# =====================================================

def main():

    if pygame is None:

        print("ERROR: Pygame installed nahi hai!")
        print("Command prompt mein yeh command chalao:")
        print("python -m pip install pygame")
        input("Enter dabao...")
        return

    pygame.init()

    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )

    pygame.display.set_caption(
        "Ganesh Ji Smooth Python Drawing"
    )

    clock = pygame.time.Clock()

    original_image = load_image()

    resized_image = resize_image(
        original_image
    )

    outline = create_outline(
        resized_image
    )

    paths = create_paths(
        outline
    )

    if not paths:

        print()
        print("ERROR: Outline create nahi hui!")
        print()
        print("Image ka naam ganesh.png hona chahiye.")
        print()

        input("Enter dabao...")
        pygame.quit()
        sys.exit()

    # Har path ki length calculate
    lengths = []

    for path in paths:

        lengths.append(
            path_length(path)
        )

    total_length = sum(
        lengths
    )

    if total_length <= 0:

        print("ERROR: Drawing path empty hai!")
        pygame.quit()
        sys.exit()

    start_time = pygame.time.get_ticks()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_r:

                    start_time = (
                        pygame.time.get_ticks()
                    )

        now = pygame.time.get_ticks()

        elapsed = (
            now - start_time
        ) / 1000

        # Smooth progress
        progress = min(
            elapsed / DRAW_TIME,
            1.0
        )

        # Smooth easing
        smooth_progress = (
            progress
            * progress
            * (
                3 - 2 * progress
            )
        )

        current_distance = (
            total_length
            * smooth_progress
        )

        screen.fill(
            BLACK
        )

        distance_done = 0

        pen_position = None

        for index, path in enumerate(paths):

            current_path_length = lengths[
                index
            ]

            path_start = distance_done

            path_end = (
                distance_done
                + current_path_length
            )

            if current_distance <= path_start:

                local_progress = 0

            elif current_distance >= path_end:

                local_progress = 1

            else:

                local_progress = (
                    current_distance
                    - path_start
                ) / current_path_length

            if local_progress > 0:

                draw_path(
                    screen,
                    path,
                    local_progress
                )

                visible_index = int(
                    (
                        len(path) - 1
                    )
                    * local_progress
                )

                visible_index = min(
                    visible_index,
                    len(path) - 1
                )

                pen_position = path[
                    visible_index
                ]

            distance_done = path_end

        # Moving golden pen/light
        if (
            pen_position is not None
            and progress < 1
        ):

            pygame.draw.circle(
                screen,
                (255, 245, 180),
                pen_position,
                5
            )

            pygame.draw.circle(
                screen,
                GOLD,
                pen_position,
                12,
                2
            )

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


# =====================================================
# START
# =====================================================

if __name__ == "__main__":

    main()