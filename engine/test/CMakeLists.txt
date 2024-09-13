
add_executable(engine_test
  test_main.cpp)

target_link_libraries(engine_test
  PRIVATE
  engine )

add_test(NAME engine_test
  COMMAND engine_test )
