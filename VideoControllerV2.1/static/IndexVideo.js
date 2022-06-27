
const videoPlayer = document.querySelector(".videoPlayer");
const video = videoPlayer.querySelector(".video");

/*const { MongoClient, ServerApiVersion } = require('mongodb'); hata verdiriyor...
const uri = "mongodb+srv://natsu:1234@cluster0.idnat.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 });
  client.connect(err => {
  const collection = client.db("test").collection("devices");
  perform actions on the collection object
  client.close();
});*/

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