window.onload = () => {
    const ros = new ROSLIB.Ros({ url: "ws://localhost:9090" });
    const element_stats = document.getElementById("status");
    video = document.getElementById("video");
    video.src = "http://0.0.0.0:8080/stream?topic=/detected_img&type=mjpeg&quality=80";
    const element_lidar_front = document.getElementById("lidar_front");
    const element_lidar_right = document.getElementById("lidar_right");
    const element_lidar_back = document.getElementById("lidar_back");
    const element_lidar_left = document.getElementById("lidar_left");
    const element_grip = document.getElementById("grip_status");
    const element_avoid = document.getElementById("avoid");
    const element_avoid_vel = document.getElementById("avoid_vel");
    const element_mission_vel = document.getElementById("mission_vel");
    
    ros.on("connection", () => {
        element_stats.innerHTML = "Connected";
        element_stats.className = "";
        element_stats.classList.add("text-success");
    });

    ros.on("error", (error) => {
        element_stats.innerHTML = `Error: ${error}`;
        element_stats.className = "";
        element_stats.classList.add("text-danger");
    });

    ros.on("close", () => {
        element_stats.innerHTML = "Close Connection";
        element_stats.className = "";
        element_stats.classList.add("text-warning");
    });

    const sensor_topic = new ROSLIB.Topic({
        ros,
        name: "/sensor_data",
        messageType: "custom_interface/SensorData"
    });

    const grip_topic = new ROSLIB.Topic({
        ros,
        name: "/status_pwr",
        messageType: "std_msgs/Bool"
    });

    const cmd_topic = new ROSLIB.Topic({
        ros,
        name: "/cmd_vel",
        messageType: "custom_interface/NaviVel"
    });

    sensor_topic.subscribe((msg) => {
        element_lidar_front.innerHTML = msg.lidar_front;
        element_lidar_right.innerHTML = msg.lidar_right;
        element_lidar_back.innerHTML = msg.lidar_back;
        element_lidar_left.innerHTML = msg.lidar_left;
    });

    grip_topic.subscribe((msg) => {
        element_grip.innerHTML = msg.data;
        if (msg.data == false){
            element_grip.className = '';
            element_grip.classList.add("text-danger")
        }else{
            element_grip.className = '';
            element_grip.classList.add("text-success")
        }
    });

    cmd_topic.subscribe((msg) => {
        element_avoid.innerHTML = msg.avoid;
        element_avoid_vel.innerHTML = msg.avoid_vel;
        element_mission_vel.innerHTML = msg.mission_vel;
    });
}