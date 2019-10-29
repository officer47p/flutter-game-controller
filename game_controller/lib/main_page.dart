import 'package:flutter/material.dart';
import 'controller_screen.dart';

class MainPage extends StatefulWidget {
  @override
  _MainPageState createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  String ip;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Game Controller"),
      ),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            TextField(
              onChanged: (value) {
                setState(() {
                  ip = value;
                });
              },
            ),
            RaisedButton(
              color: Colors.lightBlueAccent,
              textColor: Colors.white,
              child: Text("Connect"),
              onPressed: () {
//                  print(ip);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => ControllerScreen(ip),
                  ),
                );
              },
            )
          ],
        ),
      ),
    );
  }
}
