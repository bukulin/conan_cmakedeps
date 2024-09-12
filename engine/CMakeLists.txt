cmake_minimum_required(VERSION 3.15)
project(engine CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(log4cxx REQUIRED CONFIG)

add_library(engine src/engine.cpp)
target_include_directories(engine PUBLIC include)

target_link_libraries(engine PRIVATE log4cxx)

set_target_properties(engine PROPERTIES PUBLIC_HEADER "include/engine.h")
install(TARGETS engine)
