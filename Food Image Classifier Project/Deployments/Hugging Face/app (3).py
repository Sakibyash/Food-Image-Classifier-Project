import gradio as gr
from fastai.vision.all import load_learner, PILImage
import json
from typing import Iterable  # Add this import for typing hints

# Re-declare the custom class used during training
class CastToTensor:
    def __init__(self): pass
    def __call__(self, item): return item

# Load the model
LEARN = load_learner('food_model_v1.pkl')

# Load dish details
with open('dish_details.json') as f:
    DISH_DETAILS = json.load(f)

# Define the prediction function
def predict_image(img):
    img = PILImage.create(img)
    pred, pred_idx, probs = LEARN.predict(img)
    pred_label = LEARN.dls.vocab[pred_idx]
    details = DISH_DETAILS.get(pred_label, "No details available for this dish.")
    return {LEARN.dls.vocab[i]: float(probs[i]) for i in range(len(probs))}, pred_label, details

# Define the Gradio interface
title = "Food Image Classifier"
description = "Upload an image of food and the model will predict the food type."

# Examples list should contain paths to your example images
examples = ['food1.jpg', 'food2.jpg', 'food3.jpg', 'food4.jpg', 'food5.jpg']

# Custom Seafoam theme
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes

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

css = """
body {
    overflow-y: auto;
    height: 100vh;
    margin: 0;
}
.container {
    display: flex;
    flex-direction: column;
    height: 100%;
}
.content {
    flex: 1;
    overflow-y: auto;
}
.submit-button-container {
    display: flex;
    justify-content: flex-end;
    padding: 10px;
}
"""

with gr.Blocks(theme=seafoam, css=css) as interface:
    gr.Markdown(f"## {title}\n\n{description}")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil")
            examples = gr.Examples(examples=examples, inputs=image_input)

        with gr.Column():
            submit_button = gr.Button("Submit", variant="primary", elem_id="submit_button")
            label_output = gr.Label(num_top_classes=3)
            prob_output = gr.Label()  # Probabilities output
            details_output = gr.Markdown()

    def predict(img):
        pred, pred_label, details = predict_image(img)
        return pred, pred_label, details

    submit_button.click(predict_image, inputs=image_input, outputs=[label_output, prob_output, details_output])

if __name__ == "__main__":
    interface.launch()
