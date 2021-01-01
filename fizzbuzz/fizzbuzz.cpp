// Build:
// $ clang++ -std=c++17 fizzbuzz.cpp
// Run:
// $ ./a.out

#include <vector>
#include <iostream>
#include <string>

auto fizzbuzz() -> std::vector<std::string> {
    std::vector<std::string> result;
    for (int i = 1; i < (100 + 1); i++){
        if(i % 5 == 0 && i % 3 == 0){
            result.push_back("FizzBuzz");
        }
        else if(i % 5 == 0){
            result.push_back("Buzz");
        }
        else if(i % 3 == 0){
            result.push_back("Fizz");
        }
        else{
            result.push_back(std::to_string(i));
        }
    }
    return result;
}

int main()
{
    auto vec = fizzbuzz();
    for (const auto& s : vec) {
        std::cout << s << std::endl;
    }
}

// 参考サイト:
// https://www.javaer101.com/article/7698965.html
