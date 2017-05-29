#include <iostream>

int main() {
  auto start = 2*3*5*7*11*13*17*19;

  // not divisible by 4 = 2^2, so
  start *= 2;
  // not divisible by 8 = 2^3, so
  start *= 2;
  // not divisible by 9 = 3^2, so
  start *= 3;
  // not divisible by 16 = 2^4, so
  start *= 2;

  std::cout << start << std::endl;
}
