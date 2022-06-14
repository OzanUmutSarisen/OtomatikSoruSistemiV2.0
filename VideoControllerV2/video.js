const videoPlayer = document.querySelector(".videoPlayer");
const video = videoPlayer.querySelector(".video");

let time = 0;
let stopTime = 0;

setInterval(Timer,1000);

function Timer(){
    if (time == 0) {
        video.play();
    }
    if (time == 10){
        stopTime = time
        video.pause();
    }
    if (time == stopTime+5){
        video.play();
    }
    time++;
}