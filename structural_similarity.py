import cv2
from skimage.metrics import structural_similarity as ssim


# 컨투어 검출 함수
def detect_contours(image):
    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 가장자리 검출
    edges = cv2.Canny(gray, 50, 150)
    # 컨투어 검출
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 컨투어 그리기
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    return image


def match(path1, path2):
    # read the images
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    # turn images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # resize images for comparison
    img1 = cv2.resize(img1, (900, 900))
    img2 = cv2.resize(img2, (900, 900))

    similarity_value = "{:.2f}".format(ssim(img1, img2) * 100)

    return float(similarity_value)
