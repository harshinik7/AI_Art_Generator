from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/generate", methods=["GET"])
def generate_art():
    prompt = request.args.get("prompt")
    # Replace this with actual StyleGAN2 image generation logic
    generated_image_url = f"https://example.com/images/{random.randint(1, 100)}.jpg"
    return jsonify(generated_image_url)

if __name__ == "__main__":
    app.run(debug=True)

#stylegan_integ

import random

def generate_image(prompt):
    # Placeholder code; replace with actual StyleGAN2 image generation logic
    generated_image = f"https://example.com/images/{random.randint(1, 100)}.jpg"
    return generated_image

#errorhandling

@app.route("/generate", methods=["GET"])
def generate_art():
    prompt = request.args.get("prompt")
    
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    generated_image_url = generate_image(prompt)
    return jsonify({"image_url": generated_image_url})

#deployment
if __name__ == "__main__":
    app.run(debug=True)

