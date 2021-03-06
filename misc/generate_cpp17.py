#!/usr/bin/python

# Copyright (c) 2016-2022 Antony Polukhin
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

############################################################################################################################

import sys
import string

# Skipping some letters that may produce keywords or are hard to read, or shadow template parameters
ascii_letters = string.ascii_letters.replace("o", "").replace("O", "").replace("i", "").replace("I", "").replace("T", "")

PROLOGUE = """// Copyright (c) 2016-2020 Antony Polukhin
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////// THIS HEADER IS AUTO GENERATED BY misc/generate_cpp17.py                                    ////////////////
//////////////// MODIFY AND RUN THE misc/generate_cpp17.py INSTEAD OF DIRECTLY MODIFYING THE GENERATED FILE ////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#ifndef PFR_DETAIL_CORE17_GENERATED_HPP
#define PFR_DETAIL_CORE17_GENERATED_HPP
#pragma once

#include <pfr/detail/config.hpp>
#if !PFR_USE_CPP17
#   error C++17 is required for this header.
#endif

#include <pfr/detail/sequence_tuple.hpp>
#include <pfr/detail/size_t_.hpp>

namespace pfr { namespace detail {

template <class... Args>
constexpr auto make_tuple_of_references(Args&&... args) noexcept {
  return sequence_tuple::tuple<Args&...>{ args... };
}

template <class T>
constexpr auto tie_as_tuple(T& /*val*/, size_t_<0>) noexcept {
  return sequence_tuple::tuple<>{};
}

template <class T>
constexpr auto tie_as_tuple(T& val, size_t_<1>, std::enable_if_t<std::is_class< std::remove_cv_t<T> >::value>* = 0) noexcept {
  auto& [a] = val; // ====================> Boost.PFR: User-provided type is not a SimpleAggregate.
  return ::pfr::detail::make_tuple_of_references(a);
}


template <class T>
constexpr auto tie_as_tuple(T& val, size_t_<1>, std::enable_if_t<!std::is_class< std::remove_cv_t<T> >::value>* = 0) noexcept {
  return ::pfr::detail::make_tuple_of_references( val );
}

"""

############################################################################################################################
EPILOGUE = """
template <class T, std::size_t I>
constexpr void tie_as_tuple(T& /*val*/, size_t_<I>) noexcept {
  static_assert(sizeof(T) && false,
                "====================> Boost.PFR: Too many fields in a structure T. Regenerate include/pfr/detail/core17_generated.hpp file for appropriate count of fields. For example: `python ./misc/generate_cpp17.py 300 > include/pfr/detail/core17_generated.hpp`");
}

}} // namespace pfr::detail

#endif // PFR_DETAIL_CORE17_GENERATED_HPP
"""

############################################################################################################################


indexes = "    a"
print(PROLOGUE)
funcs_count = 100 if len(sys.argv) == 1 else int(sys.argv[1])
max_args_on_a_line = len(ascii_letters)
for i in range(1, funcs_count):
    if i % max_args_on_a_line == 0:
        indexes += ",\n    "
    else:
        indexes += ","

    if i >= max_args_on_a_line:
        indexes += ascii_letters[i // max_args_on_a_line - 1]
    indexes += ascii_letters[i % max_args_on_a_line]

    print("template <class T>")
    print("constexpr auto tie_as_tuple(T& val, size_t_<" + str(i + 1) + ">) noexcept {")
    if i < max_args_on_a_line:
        print("  auto& [" + indexes.strip() + "] = val; // ====================> Boost.PFR: User-provided type is not a SimpleAggregate.")
        print("  return ::pfr::detail::make_tuple_of_references(" + indexes.strip() + ");")
    else:
        print("  auto& [")
        print(indexes)
        print("  ] = val; // ====================> Boost.PFR: User-provided type is not a SimpleAggregate.")
        print("")
        print("  return ::pfr::detail::make_tuple_of_references(")
        print(indexes)
        print("  );")

    print("}\n")

print(EPILOGUE)
