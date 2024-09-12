import os
from conan import ConanFile
from conan.tools.build import can_run
from conan.tools.layout import basic_layout


class gameTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def test(self):
        if can_run(self):
            self.run("game", env="conanrun")

    def layout(self):
        basic_layout(self)
