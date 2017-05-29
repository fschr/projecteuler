#include <iostream>

int main() {
  // Principle of Inclusion-Exclusion
  int sum = 0;
  for (int i = 3; i < 1000; i += 3) sum += i;
  for (int i = 5; i < 1000; i += 5) sum += i;
  for (int i = 15; i < 1000; i += 15) sum -= i;
  std::cout << sum << std::endl;
}
