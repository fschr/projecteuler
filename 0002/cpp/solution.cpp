#include <iostream>

// 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
// Every third term is even.

int main() {
  // Algorithm to get every third term
  int sum = 0;
  int a = 1, b = 2;
  while (b < 4e6) {
    sum += b;
    a += b + b;
    b += a + a - b - b;
  }
  std::cout << sum << std::endl;
}
