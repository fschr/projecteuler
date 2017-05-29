#include <algorithm>
#include <iostream>

int main() {
  // sum of first 100 is 100(101)/2 = 5050
  constexpr auto square_of_sum = 5050*5050;

  auto sum_of_squares = 0;
  for (auto i = 1; i <= 100; ++i) sum_of_squares += i*i;

  std::cout << square_of_sum - sum_of_squares << std::endl;
}
