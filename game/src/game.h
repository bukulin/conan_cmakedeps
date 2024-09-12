#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define GAME_EXPORT __declspec(dllexport)
#else
  #define GAME_EXPORT
#endif

GAME_EXPORT void game();
GAME_EXPORT void game_print_vector(const std::vector<std::string> &strings);
