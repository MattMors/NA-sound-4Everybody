import os
import cv2
from colorthief import ColorThief

class FrameAnalyzer():

    previous_palette = []

    # def calculate_palette_difference(self, palette, previous_palette):
    #     palette_diff = []
    #     diff_values =  []
    #     for i in range(len(palette)):
    #         ch_diff = tuple(map(lambda i, j: abs(i - j), palette[i], previous_palette[i]))
    #         palette_diff.append(ch_diff)   
    #         diff_values.append(math.fsum(ch_diff))
    #     diff = sum(diff_values)

    #     print(previous_palette)
    #     print(palette)
    #     print(palette_diff)
    #     print(diff)
    #     print('\n')

    #     # return the difference between palettes
    #     return diff

    def frame_processing(self, video, timestamp, frame_id):
        difference = 0

        video.set(cv2.CAP_PROP_POS_MSEC, timestamp)
        ret, frame = video.read()

        if not ret:
            # print("FRAMES ARE OVER")
            return None, None

        # save frame as jpg
        cv2.imwrite("frame%d.jpg" % frame_id, frame)     # save frame as JPEG file      
            
        # init colorthief on new frame created
        colors = ColorThief("frame%d.jpg" % frame_id)
        palette = colors.get_palette(color_count=4)

        # for future work we can calculate the difference between palettes to get an idea of the speed of the video    
        # if frame_id != 0:
        #     difference = self.calculate_palette_difference(palette, self.previous_palette)

        self.previous_palette = palette
        
        os.remove("frame%d.jpg" % frame_id)

        return palette, difference

    
        
        
       