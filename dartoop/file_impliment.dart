import 'dart:convert';
import 'dart:io';

class Person {
  String name;
  int age;

  Person(this.name, this.age);

  String toString() {
    return 'Name: $name, Age: $age';
  }
}

void main() {
  File file = File('data.txt');
 
}
