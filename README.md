# 📹 cheonan-cctv-recorder (천안시 스마트 CCTV 레코더)

OpenCV를 이용하여 천안시 세집매 삼거리의 실시간 공공 교통 CCTV 영상을 스트리밍하고, 원하는 구간을 동영상 파일로 녹화할 수 있는 스마트 비디오 레코더입니다.

## ⚙️ 필수 기능 (Essential Features)
* **실시간 CCTV 스트리밍:** `cv.VideoCapture`를 이용해 천안시 교통정보 CCTV(RTMP 스트림)를 실시간으로 화면에 출력합니다.
* **모드 전환 (Preview / Record):** `Space` 키를 눌러 녹화(Record) 상태와 대기(Preview) 상태를 자유롭게 전환할 수 있습니다.
* **직관적인 녹화 UI:** Record 모드 진입 시, 화면 중앙 상단에 빨간색 원(🔴)이 표시되어 녹화 중임을 시각적으로 명확하게 안내합니다.
* **원본 화질 저장:** `cv.VideoWriter`를 사용하여 화면에 표시되는 UI(빨간 원)는 제외하고, 깨끗한 원본 스트림 프레임만을 `output.avi` 파일로 분리하여 저장합니다.

## 🌟 추가 구현 기능 (Extra Features)
**1. 좌우 반전 필터 (Flip Filter)**
* `F` 키를 누를 때마다 `cv.flip()` 함수가 적용되어, 실시간 화면 및 녹화되는 영상이 거울처럼 좌우로 반전되는 필터 기능을 구현하였습니다.

**2. 네트워크 지연을 고려한 FPS 보정 (FPS Adjustment)**
* 실시간 네트워크 CCTV 스트림의 실제 프레임 수신 속도와 `VideoWriter`의 기본 설정(30 FPS) 간의 차이로 인해, 저장된 영상이 배속되어 재생되는 현상이 있었습니다.
* 이를 해결하기 위해 `VideoWriter`의 저장 FPS 파라미터를 `24.0`으로 낮추어 보정함으로써, 실제 시간과 동일한 자연스러운 속도로 영상이 녹화되도록 문제를 해결하였습니다.

## ⌨️ 단축키 안내 (Usage / Hotkeys)
* `Space` : 녹화(Record) 시작 및 중지 (미리보기 모드 전환)
* `F` (또는 `f`) : 좌우 반전 필터 ON / OFF
* `ESC` : 프로그램 안전 종료 및 동영상 파일 저장 완료

## 🖼️ 실행 결과 (Screenshots & Video)

**프로그램 실행 화면 (Preview / Record 모드 및 반전 필터)**
## 🖼️ 실행 결과 (Screenshots & Video)

**1. 기본 미리보기 모드 (Preview Mode)**
![미리보기 화면](<recording image.png>)

**2. 녹화 모드 (Record Mode - 빨간 원 UI 표시)**
![녹화 중 화면](<recording image2.png>)

**3. 필터 적용 및 녹화 모드 (Flip Filter Mode - 좌우 반전)**
![반전 필터 적용 화면](<flipped image.png>)
