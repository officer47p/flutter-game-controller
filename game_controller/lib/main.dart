import 'package:flutter/material.dart';
import 'controller_screen.dart';
import 'main_page.dart';

void main() {
  runApp(GameController());
}

class GameController extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MainPage(),
    );
  }
}
