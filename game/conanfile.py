from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class gameRecipe(ConanFile):
    name = "game"
    version = "1.0.0"
    package_type = "application"

    # Optional metadata
    license = "MIT"
    author = "Norbert Bukuli"
    url = "-"
    description = "top of the graph"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"


    def requirements(self):
        self.requires("engine/1.0.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        for ref, dep in self.dependencies.items():
            self.output.warning(f">>>>>>>>>> {ref} -> {dep.package_type}")
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
