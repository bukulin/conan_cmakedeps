cmake_minimum_required(VERSION 3.15)
project(game CXX)



add_executable(game src/game.cpp src/main.cpp)



install(TARGETS game DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
