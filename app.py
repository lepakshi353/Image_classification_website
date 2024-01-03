from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import io
import wikepedia_api
import mimetypes
from PIL import Image, UnidentifiedImageError
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my.db" 
app.config["SECRET_KEY"] = "Pakha23072004"
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "avif"}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/',methods=["GET", "POST"])
def hello_world():
    result = None
    info1,info2,info3,info4,info5,info6,info7,info8=None,None,None,None,None,None,None,None
    def classify_image(file_path):
        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()

            image_type = imghdr.what(io.BytesIO(file_content))

            if image_type:
                # Your image processing code here
                return "Success"  # Replace this with your actual result
            else:
                return "Error: The uploaded file is not a valid image."
        except UnidentifiedImageError:
            return "Error: The uploaded file is not a valid image."
        except Exception as e:
            return f"Error: An unexpected error occurred - {str(e)}"

    if request.method == "POST":
        if 'pic' in request.files:
            file = request.files['pic']
            if file.filename != '':
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                print(f"Image saved to: {file_path}")
                import code_for_classification
                result = code_for_classification.classify_image(file_path)
                lst=["dandelion", "daisy", "sunflower", "tulip", "rose"]
                sci_lst=["Taraxacum","Bellis perennis","Common sunflower","Tulip","Rose"]
                info1,info2,info3,info4,info5,info6,info7,info8=wikepedia_api.get_wikipedia_intro_and_description(sci_lst[lst.index(result)])
                print(f"Classification Result: {result}")
                return render_template("index1.html",result=result,info1=info1,info2=info2,info3=info3,info4=info4,info5=info5,info6=info6,info7=info7,info8=info8)
        print("yes")    
    return render_template("index.html")
    

@app.route('/products')
def products():
    return 'This is the products website'

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__": 
    app.run(debug=True)
