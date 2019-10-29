import 'package:flutter/material.dart';
import 'package:web_socket_channel/io.dart';
import 'package:sensors/sensors.dart';

class ControllerScreen extends StatefulWidget {
  final String ip;
  ControllerScreen(this.ip);
  @override
  _ControllerScreen createState() => _ControllerScreen();
}

class _ControllerScreen extends State<ControllerScreen> {
//  var channel = IOWebSocketChannel.connect("ws://192.168.1.4:8000");
  var channel;
  AccelerometerEvent eventVar;

  void sendMsg(String msg) {
    channel.sink.add(msg);
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    channel = IOWebSocketChannel.connect("ws://${widget.ip}:8000");
    accelerometerEvents.listen((AccelerometerEvent event) {
      // Do something with the event.
      print(event);
      if (this.mounted) {
        setState(() {
          eventVar = event;
          sendMsg([eventVar.x, eventVar.y].toString());
//        channel.sink.add(eventVar.y);
        });
      }
    });
  }

  @override
  void dispose() {
    // TODO: implement dispose
    channel.sink.close();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Game Controller"),
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            Text(eventVar.toString()),
            RaisedButton(
              child: Text("press"),
              onPressed: () {
//                channel.sink.add("hello");
                Navigator.pop(context);
              },
            ),
          ],
        ),
      ),
    );
  }
}
