#include <algorithm>
#include <chrono>
#include <functional>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

template<typename T, typename E = typename T::value_type>
std::vector<std::vector<E>> combinations(const T& src) {

  std::vector<std::vector<E>> dst;

  // there are 2^cardinality combinations
  std::uint32_t num_combinations = 1 << src.size();

  // loop through all combinations
  for (std::uint32_t combo = 0; combo < num_combinations; ++combo) {

    std::vector<E> combo_vector;

    for (auto bit_index = 0; bit_index < sizeof(combo); ++bit_index) {
      if (combo & (1 << bit_index)) combo_vector.push_back(src[bit_index]);
    }

    dst.push_back(combo_vector);
  }
  return dst;
}

int main() {

  auto start_time = std::chrono::high_resolution_clock::now();

  auto power_set = combinations(std::vector<int>{ 2, 2, 5, 5, 5 });

  for (auto combo : power_set) {
    if (combo.size() == 0) continue;

    auto a = std::accumulate(combo.begin(), combo.end(), 1,
			     [](int total, int next) { return total * next; });
    auto b = 500 / a - a;
    if (a*a + 2*a*b - b*b > a*a + b*b) {

      auto end_time = std::chrono::high_resolution_clock::now();
      
      std::chrono::duration<double> total_time = end_time - start_time;

      std::cout << a*a - b*b << " + "
		<< 2*a*b << " + "
		<< a*a + b*b << " = "
		<< 2*a*a + 2*a*b << "; abc = "
		<< (a*a - b*b)*2*a*b*(a*a + b*b)
		<< std::endl
		<< "Time taken: " << total_time.count() << " seconds"
		<< std::endl;
      return 0;
    }
  }
}
