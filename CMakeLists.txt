# Copyright 2020 Peter Dimov
# Copyright (c) 2016-2025 Antony Polukhin
#
# Distributed under the Boost Software License, Version 1.0.
# https://www.boost.org/LICENSE_1_0.txt

cmake_minimum_required(VERSION 3.5...3.31)

project(pfr VERSION "${BOOST_SUPERPROJECT_VERSION}" LANGUAGES CXX)

if (PFR_USE_MODULES)
    add_library(pfr)
    target_sources(pfr PUBLIC
        FILE_SET modules_public TYPE CXX_MODULES FILES modules/boost_pfr.cppm
    )

    target_compile_features(pfr PUBLIC cxx_std_20)
    target_compile_definitions(pfr PUBLIC PFR_USE_MODULES)
    if (CMAKE_CXX_COMPILER_IMPORT_STD)
        target_compile_definitions(pfr PRIVATE PFR_USE_STD_MODULE)
        message(STATUS "Using `import std;`")
    else()
        message(STATUS "`import std;` is not available")
    endif()
    target_include_directories(pfr PUBLIC include)
else()
    add_library(pfr INTERFACE)
    target_include_directories(pfr INTERFACE include)
endif()

add_library(pfr::pfr ALIAS pfr)

enable_testing()
if (BUILD_TESTING AND EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/test/CMakeLists.txt")
    add_subdirectory(test)
endif()

if (PFR_USE_MODULES AND BUILD_TESTING)
    add_executable(pfr_module_usage modules/usage_sample.cpp)
    target_link_libraries(pfr_module_usage PRIVATE pfr::pfr)
    add_test(NAME pfr_module_usage COMMAND pfr_module_usage)

    # Make sure that mixing includes and imports is fine for different TU
    add_executable(pfr_module_usage_mu modules/usage_test_mu1.cpp modules/usage_test_mu2.cpp)
    target_link_libraries(pfr_module_usage_mu PRIVATE pfr::pfr)
    add_test(NAME pfr_module_usage_mu COMMAND pfr_module_usage_mu)
endif()

