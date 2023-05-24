from flask import Flask, jsonify, request

from structural_similarity import match

app = Flask(__name__)


@app.post("/compare_images")
def compare_images():
    try:
        # 파일 경로를 request body에서 가져오기
        data = request.get_json()
        file1_path = data["file1"]
        file2_path = data["file2"]

        # TODO: 파일 경로를 이용하여 이미지 비교 작업 수행
        similarity = match(file1_path, file2_path)

        # 결과를 JSON 형식으로 반환
        response = {"similarity": similarity}
        return jsonify(response), 200

    except Exception as e:
        # 오류 발생 시 오류 메시지와 함께 오류 상태 코드 반환
        response = {"error": str(e)}
        return jsonify(response), 400


if __name__ == "__main__":
    print("Hi")
    app.run(debug=True, port=4000)
