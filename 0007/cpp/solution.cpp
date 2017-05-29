#include <array>
#include <iostream>

constexpr std::size_t limit = 1e6;

int main() {

  std::array<bool, limit> sieve;
  std::fill(sieve.begin(), sieve.end(), true);

  // now fill the sieve
  for (auto i = 4; i < limit; i += 2) sieve[i] = false;

  for (auto p = 3; p < limit; p += 2) {
    for (auto i = p + p; i < limit; i += p) sieve[i] = false;
  }

  // now find the 10 001-st prime
  auto i = 3;
  for (auto count = 1; count < 10001; i += 2) {
    if (sieve[i]) ++count;
  }

  std::cout << i - 2 << std::endl;
}
