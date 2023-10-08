import sys
import cv2
import matplotlib.pyplot as plt
from frame_processing import *
from audio_generation import *
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

FREQUENCY = 1000
SCENE_CHANGE_THRESHOLD = 80

melody = []
ag = AudioGenerator()

def rgb_to_hsv(r, g, b): 


        r, g, b = r / 255.0, g / 255.0, b / 255.0
    
        # h, s, v = hue, saturation, value 
        cmax = max(r, g, b)    
        cmin = min(r, g, b)   
        diff = cmax-cmin      
    
        if cmax == cmin:  
            h = 0
        
        elif cmax == r:  
            h = (60 * ((g - b) / diff) + 360) % 360
    
        elif cmax == g: 
            h = (60 * ((b - r) / diff) + 120) % 360
    
        elif cmax == b: 
            h = (60 * ((r - g) / diff) + 240) % 360
    
        if cmax == 0: 
            s = 0
        else: 
            s = (diff / cmax) * 100
    
        v = cmax * 100
        return h, s, v

def hue_to_chord(hue):
    threshold_one = [15,30,45,60,75,90,105,120,135,150,165,180]
    threshold_two = [30,60,90,120,150,180,210,240,270,300,330,360]

    thresholds = threshold_one

    scale = ag.SCALES[0]
    if (hue <= thresholds[0]):
         scale = ag.SCALES[0]
    elif (hue > thresholds[0]) & (hue <= thresholds[1]):
        scale = ag.SCALES[1]
    elif (hue > thresholds[1]) & (hue <= thresholds[2]):
        scale = ag.SCALES[2]
    elif (hue > thresholds[2]) & (hue <= thresholds[3]):
        scale = ag.SCALES[3]
    elif (hue > thresholds[3]) & (hue <= thresholds[4]):    
        scale = ag.SCALES[4]
    elif (hue > thresholds[4]) & (hue <= thresholds[5]):
        scale = ag.SCALES[5]
    elif (hue > thresholds[5]) & (hue <= thresholds[6]):
        scale = ag.SCALES[6]
    elif (hue > thresholds[6]) & (hue <= thresholds[7]):
        scale = ag.SCALES[7]
    elif (hue > thresholds[7]) & (hue <= thresholds[8]):
        scale = ag.SCALES[8]
    elif (hue > thresholds[8]) & (hue <= thresholds[9]):
        scale = ag.SCALES[9]
    elif (hue > thresholds[9]) & (hue <= thresholds[10]):
        scale = ag.SCALES[10]
    elif (hue > thresholds[10]) & (hue <= thresholds[11]):
        scale = ag.SCALES[11]
    else:
        scale = ag.SCALES[0]
    
    return scale

def finalize_video(base_name):
    # Open the video and audio
    video_clip = VideoFileClip(base_name)
    audio_clip = AudioFileClip('../res/audio/tones.wav')

    # Concatenate the video clip with the audio clip
    final_clip = video_clip.set_audio(audio_clip)
    # Export the final video with audio
    final_clip.write_videofile('../res/video/final_video' + ".mp4")

video_name = '../res/video/' + sys.argv[1]
video = cv2.VideoCapture(video_name)
success, _ = video.read()

if not success:
    raise Exception("Error: Failed to read video file")

# use to visualize the palette's plot
# fig, ax = plt.subplots()

millisec = 0
frame_number = 0

fa = FrameAnalyzer()

while True:
    palette, difference = fa.frame_processing(video, millisec, frame_number)
    if palette == None:
        break
    
    # for future works we can use the brightness to change in a deterministic way the octaves of the notes
    hue, _, lightness = rgb_to_hsv(*palette[3])
    note = hue_to_chord(hue)
    melody.append(note)

    # to show the palette
    # plt.imshow([[palette[i] for i in range(4)]])
    # plt.show()

    previous_palette = palette
    millisec += FREQUENCY
    frame_number +=1

ag.generate_melody(melody)

finalize_video(video_name)
