# Environment
gentoo linux
conan-2.7.1
gcc-7.5.0
binutils-2.33.1
glibc-2.34
linux-headers-5.15
```
$ conan profile show 
Host profile:
[settings]
arch=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=gnu14
compiler.libcxx=libstdc++11
compiler.version=7
os=Linux
[conf]


Build profile:
[settings]
arch=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=gnu14
compiler.libcxx=libstdc++11
compiler.version=7
os=Linux
[conf]
```

# How to reproduce failing build in engine?
```
cd engine
conan create . -o *:shared=True
# or
conan build . -o *:shared=True
```
