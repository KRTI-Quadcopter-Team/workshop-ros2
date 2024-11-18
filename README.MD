# ROS 2 Packages Workshop Quadcopter
Repository ini digunakan untuk template packages ros2 drone programming di workshop Quadcopter Robotiik 2024. Harap gunakan repository ini untuk pembelajaran dan kembangkan dari waktu ke waktu. Kami tim Quadcopter Robotiik berharap besar pada kalian penerus tim. Have a nice day.😊

## Installation
Pertama kalian harus menginstall lengkap Ubuntu 22 dan [ROS2](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)
### Install Dependencies
```
$ sudo apt update
$ sudo apt install python3-pip ros-humble-rosbridge-suite ros-humble-web-vide-server
$ pip install fastapi
$ pip install uvicorn
$ pip install pyyaml
```
install nvm seperti dokumentasi dari [robotics-ui](https://github.com/sciotaio/robotics-ui)
```
$ sudo apt update
$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
$ export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
$ nvm install node
```
### Make ws and Clone Repository
```
$ mkdir your_ws
$ cd your_ws
$ git clone --recurse-submodules https://github.com/Robotiik-Quadcopter-Team/workshop-ros2.git src
```
### Build All Packages
```
$ cd ~/your_ws
$ colcon build
```
## Usage
Untuk menjalankan seluruh node yang diperlukan cukup jalankan launch file di packages ***drone_bringup***
```
ros2 launch drone_bringup sim_bringup.launch.yaml
```
## Note
Repository ini akan selalu diupdate selama workshop ini. Diharapkan para anggota dapat berkontribusi untuk mengupdate sesuai dengan kebutuhan yang akan datang.
