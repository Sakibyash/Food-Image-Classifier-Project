from fastai.vision.all import load_learner
import gradio as gr
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes
from collections.abc import Iterable 

# Custom Seafoam theme
class Seafoam(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.emerald,
        secondary_hue: colors.Color | str = colors.blue,
        neutral_hue: colors.Color | str = colors.blue,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_md,
        text_size: sizes.Size | str = sizes.text_lg,
        font: fonts.Font | str | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("Quicksand"),
            "ui-sans-serif",
            "sans-serif",
        ),
        font_mono: fonts.Font | str | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("IBM Plex Mono"),
            "ui-monospace",
            "monospace",
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            body_background_fill="repeating-linear-gradient(45deg, *primary_200, *primary_200 10px, *primary_50 10px, *primary_50 20px)",
            body_background_fill_dark="repeating-linear-gradient(45deg, *primary_800, *primary_800 10px, *primary_900 10px, *primary_900 20px)",
            button_primary_background_fill="linear-gradient(90deg, *primary_300, *secondary_400)",
            button_primary_background_fill_hover="linear-gradient(90deg, *primary_200, *secondary_300)",
            button_primary_text_color="white",
            button_primary_background_fill_dark="linear-gradient(90deg, *primary_600, *secondary_800)",
            slider_color="*secondary_300",
            slider_color_dark="*secondary_600",
            block_title_text_weight="600",
            block_border_width="3px",
            block_shadow="*shadow_drop_lg",
            button_shadow="*shadow_drop_lg",
            button_large_padding="32px",
        )

seafoam = Seafoam()

# Food labels
food_labels = [
    'Baked Potato', 'Crispy Chicken', 'Donut', 'Fries', 'Hot Dog', 'Sandwich', 'Taco', 'Taquito',
    'Apple Pie', 'Burger', 'Butter Naan', 'Chai', 'Chapati', 'Cheesecake', 'Chicken Curry',
    'Chole Bhature', 'Dal Makhani', 'Dhokla', 'Fried Rice', 'Ice Cream', 'Idli', 'Jalebi', 
    'Kaathi Rolls', 'Kadai Paneer', 'Kulfi', 'Masala Dosa', 'Momos', 'Omelette', 'Paani Puri', 
    'Pakode', 'Pancakes', 'Quesadilla', 'Ratatouille', 'Samosa', 'Spring Rolls', 'Stuffed Bell Peppers',
    'Tandoori Chicken', 'Uttapam', 'Veggie Burger', 'Waffles', 'Zucchini Bread'
]

# Load model
model = load_learner("food_model_v2.pkl")

# Prediction function
def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(food_labels, map(float, probs)))

# Gradio interface
image = gr.Image()
label = gr.Label()
examples = ["food1.jpg", "food2.jpg", "food3.jpg", "food4.jpg"]

# Interface with Seafoam theme
iface = gr.Interface(
    fn=recognize_image,
    inputs=image,
    outputs=label,
    examples=examples,
    theme=seafoam  # Apply Seafoam theme here
)

# Launch the app
iface.launch(inline=False, share=True)
