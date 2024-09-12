#include "game.h"
#include <vector>
#include <string>

int main() {
    game();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    game_print_vector(vec);
}
