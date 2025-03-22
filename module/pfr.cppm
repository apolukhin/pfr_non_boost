// Copyright (c) 2016-2024 Antony Polukhin
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

// To compile manually use a command like the folowing:
// clang++ -I ../include -std=c++20 --precompile -x c++-module pfr.cppm

#define PFR_BEGIN_MODULE_EXPORT export {
#define PFR_END_MODULE_EXPORT }

#ifndef PFR_HAS_STD_MODULE
module;
#include <array>
#include <cstddef>
#include <functional>
#include <iomanip>
#include <iostream>
#include <memory>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>
#include <variant>
#endif

export module PFR;

#ifdef PFR_HAS_STD_MODULE
import std;
#endif

#ifdef __clang__
#   pragma clang diagnostic ignored "-Winclude-angled-in-module-purview"
#endif

#ifdef PFR_ATTACH_TO_GLOBAL_MODULE
extern "C++" {
#include <pfr.hpp>
}
#else
#include <pfr.hpp>
#endif
