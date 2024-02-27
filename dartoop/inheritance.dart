class Student {
  String course;

  Student(this.course);

  void takesComputer_Science() {}
}

class Boy extends Student {
  Boy(String course) : super(course);
  void takesComputer_Science() {
    print("Am a IT Major");
  }
}

class Girl extends Student {
  Girl(String course) : super(course);
  void takesComputer_Science() {
    print("Am a Data Analysit ");
  }
}

void main() {
  Boy boy = Boy("Barrack");
  print(boy.course); 
  boy.takesComputer_Science(); 
}
