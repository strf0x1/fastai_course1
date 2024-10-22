import gradio as gr
from fastai.vision.all import *

# Load the trained model
learn_inf = load_learner('export.pkl')

def predict_image(image):
    # Make prediction
    result = learn_inf.predict(image)
    # Return the prediction result (assuming first element is class prediction)
    return str(result[0])

# Create the Gradio interface
iface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(),  # This creates an image upload component
    outputs=gr.Text(label="Prediction"),
    title="Image Classifier",
    description="Upload an image to get a prediction."
)

# Launch the app
if __name__ == "__main__":
    iface.launch()
