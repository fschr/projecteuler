#include <chrono>
#include <deque>
#include <iostream>
#include <utility>

template<typename T>
bool is_palindrome(T n) {
  std::deque<T> d;
  while (n != 0) {
    d.push_back(n % 10);
    n /= 10;
  }
  for (auto p = std::make_pair(d.begin(), d.rbegin());
       p.first < (p.second.base() - 1); ++p.first, ++p.second) {
    if (*p.first != *p.second) return false;
  }
  return true;
}

int main() {

  auto start_time = std::chrono::high_resolution_clock::now();

  // this palindrome must be a multiple of 11
  // n starts at largest multiple of 11 <= 999*999
  auto n = 999*999 - 4;

  // search through palindromes in descending order
  for(; n >= 100*100; n -= 11) {

    if (!is_palindrome(n)) continue;

    // check if it's a product of two 3-digit numbers
    for (auto i = 999; n / i <= 999 and i >= 100; --i) {
      if ((n % i == 0) and (n / i >= 100)) {

	auto end_time = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> total_time =  end_time - start_time;

	std::cout << i << "*" << n / i << " = " << n << std::endl
		  << "Time taken: " << total_time.count()
		  << " seconds" << std::endl;

	return 0;
      }
    }
  }

  std::cout << "Incorrect algorithm: no solution found!" << std::endl;
}
