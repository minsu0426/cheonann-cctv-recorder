import cv2 as cv

def main():
    rtsp_url = 'rtmp://210.99.70.120/live/cctv004.stream' 
    
    video = cv.VideoCapture(rtsp_url)
    
    if not video.isOpened():
        print("주소상태 다시 확인")
        return

    fps = video.get(cv.CAP_PROP_FPS)
    if fps == 0 or fps != fps: 
        fps = 60.0
    wait_msec = int(1 / fps * 10)

    width = int(video.get(3))
    height = int(video.get(4))
    
    # 간혹 폭과 높이를 0으로 불러와서 비디오 라이터가 터지는 것을 방지
    if width == 0 or height == 0:
        print("비디오 해상도를 불러오지 못했습니다")
        return
    save_fps = 12.0
    video_writer = cv.VideoWriter('output.avi', cv.VideoWriter_fourcc(*'XVID'), save_fps, (width, height))

    is_recording = False
    is_flipped = False
    
    while True:
        valid, img = video.read()
        
        if not valid:
            print("정상 종료")
            break
        
        if is_flipped:
            img = cv.flip(img, 1)
            
        display_img = img.copy()

        # Record 모드일 때만 화면 중앙 상단에 빨간색 원 그리기
        if is_recording:
            center_x = int(width / 2)
            cv.circle(display_img, (center_x, 50), 10, (0, 0, 255), -1)
            
            video_writer.write(img)

        cv.imshow('Cheonan Traffic watcher', display_img)

        key = cv.waitKey(wait_msec)
        
        if key == 27:
            print("프로그램 종료")
            break
        elif key == ord(" "): 
            is_recording = not is_recording
            if is_recording:
                print("▶ Record 시작")
            else:
                print("■ Record 중지")
        elif key == ord('f') or key == ord('F'): 
            is_flipped = not is_flipped

    video_writer.release()
    video.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()