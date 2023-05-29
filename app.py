from flask import Flask, jsonify, request

from torch_siamese_net.siamese_net import checkSimilarity

app = Flask(__name__)


@app.get("/compare_images")
def compare_images():
    try:
        # 파일 경로를 query string에서 가져오기
        file1_path = request.args.get("file1")
        file2_path = request.args.get("file2")

        # 이미지 유사도 계산
        # similarity = match(file1_path, file2_path)
        similarity = checkSimilarity(file1_path, file2_path)

        # 결과를 JSON 형식으로 반환
        response = {"similarity": similarity}
        return jsonify(response), 200

    except Exception as e:
        # 오류 발생 시 오류 메시지와 함께 오류 상태 코드 반환
        response = {"error": str(e)}
        return jsonify(response), 400


if __name__ == "__main__":
    app.run(debug=True, port=4000)
