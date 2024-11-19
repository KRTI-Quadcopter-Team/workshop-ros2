# ROS 2 Packages Workshop Quadcopter
Repository ini digunakan untuk template packages ros2 drone programming di workshop Quadcopter Robotiik 2024. Harap gunakan repository ini untuk pembelajaran dan kembangkan dari waktu ke waktu. Kami tim Quadcopter Robotiik berharap besar pada kalian penerus tim. Have a nice day.😊

## Node Graph
![Node Graph now version](https://github.com/Robotiik-Quadcopter-Team/workshop-ros2/blob/main/img/node_graph_v1.jpg?raw=true)

## Installation
Pertama kalian harus menginstall lengkap Ubuntu 22 dan [ROS2](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)
### Install Dependencies
```
$ sudo apt update
$ sudo apt install python3-pip ros-humble-rosbridge-suite ros-humble-web-video-server
$ pip install opencv-python
```
### Make ws and Clone Repository
```
$ mkdir your_ws
$ cd your_ws
$ git clone https://github.com/Robotiik-Quadcopter-Team/workshop-ros2.git src
```
### Build All Packages
```
$ cd ~/your_ws
$ colcon build
```
## Usage
Untuk menjalankan seluruh node yang diperlukan cukup jalankan launch file di packages ***drone_bringup***
```
$ ros2 launch drone_bringup sim_bringup.launch.yaml
```
Mengakses Web ui dapat dilakukan secara manual dengan menjalankan server http dan membuka situs di browser
```
$ cd ~/your_ws/src/simulation_packages/web
$ python server.py
# open your browser to http://127.0.0.1:5050
```
## Note
Repository ini akan selalu diupdate selama workshop ini. Diharapkan para anggota dapat berkontribusi untuk mengupdate sesuai dengan kebutuhan yang akan datang.
