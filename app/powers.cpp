#include <iostream>

double powers(int base, int exp) {
  double result = 1.0;

  if (exp > 0) {
    for (int i = 0; i < exp; i++) {
      result *= base;
    }
  } else if (exp < 0) {
    for (int i = 0; i > exp; i--) {
      result /= base;
    }
  }

  return result;
}

int main() {
  std::cout << powers(2, 4) << "\n";
  std::cout << powers(2, 0) << "\n";
  std::cout << powers(2, -4) << "\n";
  std::cout << powers(2, -3) << "\n";
  std::cout << powers(-2, -3) << "\n";
  std::cout << powers(-2, 3) << "\n";
  std::cout << powers(-2, 4) << "\n";
  return 0;
}
