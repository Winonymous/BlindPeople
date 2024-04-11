import serial
from describe_scene import DescribeScene
import cv2 
from play_text import PlayText
from get_person import get_match
  
  
# define a video capture object 
vid = cv2.VideoCapture(0) 

def main():
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
    ser.reset_input_buffer()
    # desriptor = DescribeScene()
    player = PlayText()
    print("Finish Loading Models")
    
    while True:
        # Capture the video frame 
        # by frame 
        ret, frame = vid.read() 
        cv2.imshow('frame', frame) 

        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            if line == 'describe':
                print("desc")
                

                if(ret):
                    # Display the resulting frame 
                    # caption = desriptor.caption(frame)
                    caption = "Hello"
                    # print(caption)
                    player.generate_play(caption)
            elif line == 'recognizeface':
                if(ret):
                    match = get_match(frame)
                    if(match):
                        player.generate_play("Person Known")

                        name = match.split('.')[0]

                        player.generate_play(name)
                    else:
                        player.generate_play("Person Unknown")
        
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    # After the loop release the cap object 
    vid.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows() 


if __name__ == '__main__':
    main()