#include <chrono>
#include <iostream>

template<typename T>
T largest_prime_factor(T n) {

  auto lpf = 1;

  if (n % 2 == 0) {
    lpf = 2;
    while (n % 2 == 0) n /= 2;
  }

  
  for (auto p = 3; n > 1; p += 2) {

    if (n % p == 0) {
      lpf = p;
      while (n % p == 0) n /= p;
    }

  }

  return lpf;
}

int main() {

  auto start_time = std::chrono::high_resolution_clock::now();

  auto solution = largest_prime_factor(600851475143);

  auto end_time = std::chrono::high_resolution_clock::now();
  std::chrono::duration<double> total_time = end_time - start_time;


  std::cout << solution
	    << std::endl
	    << "Time taken: " << total_time.count() << " seconds"
	    << std::endl;
}
