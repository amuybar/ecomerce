abstract class Country {
  double population();
}

class Kenya implements Country {
  double men;
  double women;
  Kenya(this.men, this.women);
  double population() {
    return men + women;
  }
}

void main() {
  Kenya kenya = Kenya(23000000, 30000000);
  print(kenya.population()); 
}
