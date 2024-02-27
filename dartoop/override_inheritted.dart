class Sexuality {
  void hetero() {
    print("Loves Opposite");
  }
}

class Homo extends Sexuality {
  void hetero() {
    print("Loves Same");
  }
}

void main() {
  Homo homo = Homo();
  homo.hetero(); 
}
