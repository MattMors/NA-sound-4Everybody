import os
import cv2
from colorthief import ColorThief
import numpy as np

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

    def frame_segmentation(self, video, timestamp, frame_id):
        video.set(cv2.CAP_PROP_POS_MSEC, timestamp)
        ret, frame = video.read()

        if not ret:
            print("FRAMES ARE OVER")
            return True

        # //////////////////////// SEGMENTATION /////////////////////////////

        # Set the parameters for the mean shift algorithm
        # You may need to adjust these parameters based on your specific image and requirements
        spatial_radius = 30
        color_radius = 70
        max_pyr_level = 3

        kernel = np.ones((7, 7), np.uint8)
        eroded_image = cv2.erode(frame, kernel, iterations=2)
        # dilated_img = cv2.dilate(eroded_image, kernel, iterations=20)

        kernel_size = (5, 5)  # You can adjust the kernel size based on your requirements
        blurred_image = cv2.GaussianBlur(eroded_image, kernel_size, 0)

        # Apply the mean shift algorithm
        segmented_image = cv2.pyrMeanShiftFiltering(blurred_image, spatial_radius, color_radius, max_pyr_level)

        eroded_image = cv2.erode(segmented_image, kernel, iterations=10)

        # segmented_image = cv2.pyrMeanShiftFiltering(segmented_image, spatial_radius, color_radius, max_pyr_level)
        # _,  thresh = cv2.threshold(gray, np.mean(gray), 255, cv2.THRESH_TRUNC)
        cv2.imshow("threshold", segmented_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # //////////////////////// END SEGMENTAION ///////////////////////////

    def frame_processing(self, video, timestamp, frame_id):
        difference = 0

        video.set(cv2.CAP_PROP_POS_MSEC, timestamp)
        ret, frame = video.read()

        if not ret:
            print("FRAMES ARE OVER")
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

    
        
        
       