import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

BrushSiz = 10
LColor, RColor = (255, 0, 0), (0, 0, 255) # 파랑, 빨강

def painting(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),BrushSiz, LColor, -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),BrushSiz, RColor, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),BrushSiz, LColor, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img,(x,y),BrushSiz, RColor, -1)

    cv.imshow('Painting', img)

cv.namedWindow('Painting')
cv.imshow('Painting', img)


cv.setMouseCallback('Painting', painting)


while(True):
    key = cv.waitKeyEx(1)
    if key == 43 and BrushSiz < 50:
        BrushSiz += 1
    elif key == 45 and BrushSiz > 2:
        BrushSiz -= 1
    elif key == ord('q'):
        cv.destroyAllWindows()
        break

