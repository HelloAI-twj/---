import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import paddlex as pdx
class car_detect():
    def __init__(self,video_file,save_dir,revolution):
        super(car_detect, self).__init__()
        self.videofile=video_file#预测视频地址
        self.save_dir=save_dir#保存视频地址
        self.revolution = revolution#视频分辨率
    def detection(self):
        model = pdx.deploy.Predictor('H:/quant_model', use_gpu=False)
        capture = cv2.VideoCapture(self.videofile)
        fourcc=cv2.VideoWriter_fourcc(*'XVID')
        outfile=cv2.VideoWriter(self.save_dir,fourcc,25,self.revolution)
        font=ImageFont.truetype('H:/simhei.ttf',60,encoding='utf-8')
        while True:
            # 取出一帧数据
            ret, frame_rgb = capture.read()
            if frame_rgb is None:
                break

            # PaddleX要求的输出是bgr格式
            frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR).astype('float32')

            # 进行预测
            result = model.predict(frame_bgr)
            num = 0  # 车辆计数器
            for j in result:
                if j['category'] == 'car' and j['score'] > 0.3:
                    num += 1
                if j['score'] > 0.3:
                    cv2.rectangle(frame_rgb, (int(j['bbox'][0]), int(j['bbox'][1])),
                                  (int(j['bbox'][0] + j['bbox'][2]), int(j['bbox'][1] + j['bbox'][3])), (0, 255, 0), 2)
                    cv2.putText(frame_rgb, '{}'.format(j['category']), (int(j['bbox'][0]), int(j['bbox'][1])),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
                    cv2.putText(frame_rgb, '{0:.2f}'.format(float(j['score'])),
                                (int(j['bbox'][0] + 45), int(j['bbox'][1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0),
                                2, cv2.LINE_AA)
                    frame_rgb = self.trafficlight(frame_rgb, j['bbox'])
                else:
                    continue

                if j['score'] > 0.3:
                    # 如果矩形框与车道线相交，则判定为压线并用ya来表示
                    b = self.check([363, 648], [100, 894], [j['bbox'][0], j['bbox'][1], (j['bbox'][0] + j['bbox'][2]),
                                                            (j['bbox'][1] + j['bbox'][3])])
                    d = self.check([591, 654], [334, 1061], [j['bbox'][0], j['bbox'][1], (j['bbox'][0] + j['bbox'][2]),
                                                             (j['bbox'][1] + j['bbox'][3])])
                    if b == 1 or d == 1:
                        cv2.putText(frame_rgb, 'ya', (int(j['bbox'][0]), int(j['bbox'][1] + 20)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
            pilimg = Image.fromarray(frame_rgb)
            draw = ImageDraw.Draw(pilimg)
            draw.text((102, 450), '车辆数:{}'.format(num), (0, 0, 255), font=font)
            outfile.write(np.array(pilimg))
            print('2')
        capture.release()
        return 1
    def trafficlight(self, img, pos):
        result = [img[96:123, 1076:1085], img[95:125, 1104:1114], img[96:124, 1132:1141]]  # 一张图的三个红绿灯
        loc = ['left', 'straight', 'right']
        green = 0#像素计数器
        red = 0
        yellow = 0
        for j, image in enumerate(result):
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            z = range(0, hsv.shape[0])
            d = range(0, hsv.shape[1])
            # 对一个指示灯的颜色进行遍历
            for x in z:
                for y in d:
                    b = hsv[x, y]
                    if (b[0] >= 35 and b[0] <= 77) or (b[0] >= 78 and b[0] <= 99):  # H阈值
                        if b[1] >= 43 and b[0] <= 255:  # S阈值
                            if b[2] > 46 and b[2] <= 255:  # v阈值
                                green += 1
                    if (b[0] >= 156 and b[0] <= 180):
                        if b[1] >= 43 and b[0] <= 206:
                            if b[2] > 46 and b[2] <= 237:
                                red += 1

                    if (b[0] >= 11 and b[0] <= 25) or (b[0] >= 26 and b[0] <= 34):
                        if b[1] >= 43 and b[0] <= 255:
                            if b[2] > 46 and b[2] <= 255:
                                yellow += 1
            light = max(green, red, yellow)  # 最大值即为红绿灯颜色
            if light == 0:
                break
            elif light == green:
                cv2.putText(img, str(loc[j]) + ':green', (102, 340 + 50 * j), cv2.FONT_HERSHEY_SIMPLEX, 2,
                            (46, 195, 34), 4, cv2.LINE_AA)
            elif light == red:
                cv2.putText(img, str(loc[j]) + ':red', (102, 340 + 50 * j), cv2.FONT_HERSHEY_SIMPLEX, 2,
                            (0, 0, 255), 4, cv2.LINE_AA)
                #当为红灯时，若汽车在某一区域内则判定为闯红灯并用w!!来表示
                if (pos[0] + pos[2] / 2 > 378 and pos[0] + pos[2] / 2 < 1422) and (
                        pos[1] > 270 and pos[1] < 638) and pos[2] / pos[3] < 2:
                    cv2.putText(img, 'w!!', (int(pos[0] + pos[2] / 2), int(pos[1] + pos[3] / 2)),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
            elif light == yellow:
                cv2.putText(img, str(loc[j]) + ':yellow', (102, 340 + 50 * j), cv2.FONT_HERSHEY_SIMPLEX, 2,
                            (0, 255, 255), 4, cv2.LINE_AA)
            green = 0
            yellow = 0
            red = 0
        return img

    def cross(self, p1, p2, p3):  # 叉积判定
        x1 = p2[0] - p1[0]
        y1 = p2[1] - p1[1]
        x2 = p3[0] - p1[0]
        y2 = p3[1] - p1[1]
        return x1 * y2 - x2 * y1

    def segment(self, p1, p2, p3, p4):  # 判断两线段是否相交
        # 矩形判定，以l1、l2为对角线的矩形必相交，否则两线段不相交
        if (max(p1[0], p2[0]) >= min(p3[0], p4[0])  # 矩形1最右端大于矩形2最左端
                and max(p3[0], p4[0]) >= min(p1[0], p2[0])  # 矩形2最右端大于矩形1最左端
                and max(p1[1], p2[1]) >= min(p3[1], p4[1])  # 矩形1最高端大于矩形2最低端
                and max(p3[1], p4[1]) >= min(p1[1], p2[1])):  # 矩形2最高端大于矩形1最低端
            if (self.cross(p1, p2, p3) * self.cross(p1, p2, p4) <= 0 and self.cross(p3, p4, p1) * self.cross(p3, p4,
                                                                                                             p2) <= 0):
                D = 1
            else:
                D = 0
        else:
            D = 0
        return D

    def check(self, l1, l2, sq):
        # step 1 check if end point is in the square
        if (l1[0] >= sq[0] and l1[1] >= sq[1] and l1[0] <= sq[2] and l1[1] <= sq[3]) or (
                l2[0] >= sq[0] and l2[1] >= sq[1] and l2[0] <= sq[2] and l2[1] <= sq[3]):
            return 1
        else:
            # step 2 check if diagonal cross the segment
            p1 = [sq[0], sq[1]]
            p2 = [sq[2], sq[3]]
            p3 = [sq[2], sq[1]]
            p4 = [sq[0], sq[3]]
        if self.segment(l1, l2, p1, p2) or self.segment(l1, l2, p3, p4):
            return 1
        else:
            return 0






