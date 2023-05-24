from flask import Flask, request

app = Flask(__name__)


@app.route("/compare_images", methods=["POST"])
def compare_images():
    file1 = request.files["file1"]
    file2 = request.files["file2"]

    # 이미지 처리 및 비교 작업 수행
    filename1 = file1.filename
    filename2 = file2.filename

    return f"Image 1: {filename1}, Image 2: {filename2}"


if __name__ == "__main__":
    app.run()
