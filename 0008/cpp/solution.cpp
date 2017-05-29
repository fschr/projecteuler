#include <array>
#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <numeric>

int main() {

  std::fstream fs;
  fs.open("input_file");

  if (!fs.is_open() || !fs.good()) {
    std::cerr << "Failed to open input_file" << std::endl;
  }

  constexpr auto num_adjacent = 13;

  std::array<std::uint64_t, num_adjacent> ring_buffer;
  std::fill(std::begin(ring_buffer), std::end(ring_buffer), 1);
  auto pos = 0;
  
  std::uint64_t product = 1, max_product = 1;

  char current_char;
  while (fs.get(current_char)) {

    if (current_char == '\n') continue;

    ring_buffer[pos] = (std::uint64_t)current_char - 48; // convert char digit to int
    pos = (pos + 1) % num_adjacent;
    
    product = std::accumulate(std::begin(ring_buffer), std::end(ring_buffer),
			      (std::uint64_t)1, std::multiplies<std::uint64_t>());

    if (product > max_product) max_product = product;
  }

  std::cout << max_product << std::endl;
}
