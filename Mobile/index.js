const port = 8080;

const net = require("net");
const express = require("express");
const app = express();
app.use(express.static("src"));


const http = require("http").createServer(app);
const socketio = require("socket.io")(http);

http.listen(port, () =>
  console.log(`Example app listening at http://localhost:${port}`)
);

let matlab_sender = null;

socketio.on("connection", (socket) => {
  socket.on("update", (dane) => {
    console.log(dane);
    write2Matlab(dane);
  });
  console.log("new user");
});

net.createServer(function (session) {
  matlab_sender = session;

  session.on("data", (data) => {
    const liczba = data.readDoubleBE();
    console.log(" " + liczba);

    socketio.sockets.emit("response", liczba);
  });
  session.on("error", console.log);
}).listen(5555, "0.0.0.0");;

function write2Matlab(tablica) {
	const buffor = Buffer.allocUnsafe(8);
  
	for (let i = 0; i < tablica.length; ++i) {
	  buffor.writeDoubleBE(tablica[i]);
	  matlab_sender.write(buffor);
	}
}