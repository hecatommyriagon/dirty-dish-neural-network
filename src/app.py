from flask import Flask, render_template, request
import os
import make_classification

app = Flask(__name__)

# Initialize global variable
classification = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global classification  # Declare 'classification' as global
    if request.method == "POST":
        # Handle the file upload
        file = request.files.get("file")
        if file and file.filename != '':
            # Save the uploaded file to a desired location
            upload_folder = "src/uploads"
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            
            filepath = os.path.join(upload_folder, file.filename)
            file.save(filepath)

            # Query and update the global classification variable
            try:
                result = make_classification.classify(input_path=filepath, output_path=f"src/data/cache/{file.filename}")
                classification = "DIRTY" if result else "CLEAN"
            except Exception as e:
                classification = f"Error in classification: {str(e)}"

    return render_template(
        "index.html",
        classification=classification
    )

if __name__ == "__main__":
    app.run(debug=True)
