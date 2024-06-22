from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # معالجة رفع الصور هنا
    return "تم رفع الصورة بنجاح!"

@app.route('/post_text_link', methods=['POST'])
def post_text_link():
    # معالجة نشر النصوص والروابط هنا
    return "تم نشر النص أو الرابط بنجاح!"

@app.route('/upload_python', methods=['POST'])
def upload_python():
    # معالجة رفع الملفات Python هنا
    return "تم رفع الملف الخاص بالبايثون بنجاح!"

if __name__ == '__main__':
    app.run(debug=True)