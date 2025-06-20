// Copyright (c) 2016-2025 Antony Polukhin
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

// To compile manually use a command like the folowing:
// clang++ -std=c++20 -fmodule-file=pfr.pcm pfr.pcm usage_sample.cpp

//[pfr_module_example
#include <iostream>
#include <iomanip>
#include <string>

import pfr;

struct some_person {
    std::string name;
    unsigned birth_year;
};

int main() {
    some_person val{"Edgar Allan Poe", 1809};

    std::cout << pfr::get<0>(val)                // No macro!
        << " was born in " << pfr::get<1>(val);  // Works with any aggregate!

    std::cout << '\n' << pfr::io(val);           // Outputs: {"Edgar Allan Poe", 1809}
    std::cout << "\n." << pfr::get_name<0, some_person>()
        << '=' << val.name << '\n';                     // Outputs: .name=Edgar Allan Poe
}
//]
