import cv2
import numpy as np
# pyzbar import
from pyzbar.pyzbar import decode

def decoder(image):
    # We're using BGR color format
    trans_img = cv2.cvtColor(image,0)
    BarCode = decode(trans_img)

    for obj in BarCode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        # box size
        pts = pts.reshape((-1, 1, 2))
        thickness = 2
        isClosed = True
        # fill color (border)
        line_color = (0, 0, 255)
        cv2.polylines(image, [pts], isClosed, line_color, thickness)
        
        
        # read qr codes (detect and decode qr codes)
        BarCodeData = obj.data.decode("utf-8")
        BarCodeType = obj.type
        the_text = "Data: " + str(BarCodeData)
        
        org = (x,y)
        text_color = (255, 180, 180)
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(image, the_text, org, font, 0.9, text_color, 2)
        # data print 
        print("The Data is: " + BarCodeData +" & the Type is: " + BarCodeType)

if __name__ == "__main__":
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        decoder(frame)
        cv2.imshow('Image', frame)
        code = cv2.waitKey(1)
        if code == ord('q'):
            break

    cv2.destroyAllWindows()