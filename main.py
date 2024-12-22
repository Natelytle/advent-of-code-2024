from SmallKeypad import SmallKeypad
from BigKeypad import BigKeypad

zero_position = (1, 0)
activate_position = (2, 0)
one_position = (0, 1)
two_position = (1, 1)
three_position = (2, 1)
four_position = (0, 2)
five_position = (1, 2)
six_position = (2, 2)
seven_position = (0, 3)
eight_position = (1, 3)
nine_position = (2, 3)

humanKeypad = SmallKeypad(None)
botKeypad1 = SmallKeypad(humanKeypad, "debug")
botKeypad2 = SmallKeypad(botKeypad1)
numericKeypad = BigKeypad(botKeypad2)

botKeypad1.total_combination = []

print((numericKeypad.find_shortest_path(*five_position) +
      numericKeypad.find_shortest_path(*four_position) +
      numericKeypad.find_shortest_path(*zero_position) +
      numericKeypad.find_shortest_path(*activate_position)) * 540)

botKeypad1.total_combination = []

print((numericKeypad.find_shortest_path(*eight_position) +
      numericKeypad.find_shortest_path(*three_position) +
      numericKeypad.find_shortest_path(*nine_position) +
      numericKeypad.find_shortest_path(*activate_position)) * 839)

botKeypad1.total_combination = []

print((numericKeypad.find_shortest_path(*six_position) +
      numericKeypad.find_shortest_path(*eight_position) +
      numericKeypad.find_shortest_path(*two_position) +
      numericKeypad.find_shortest_path(*activate_position)) * 682)

botKeypad1.total_combination = []

print((numericKeypad.find_shortest_path(*eight_position) +
      numericKeypad.find_shortest_path(*two_position) +
      numericKeypad.find_shortest_path(*six_position) +
      numericKeypad.find_shortest_path(*activate_position)) * 826)

botKeypad1.total_combination = []

print((numericKeypad.find_shortest_path(*nine_position) +
      numericKeypad.find_shortest_path(*seven_position) +
      numericKeypad.find_shortest_path(*four_position) +
      numericKeypad.find_shortest_path(*activate_position)) * 974)

print("")

print(len("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"))
print(len("<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A"))
print(len("<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))
print(len("<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A"))
print(len("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))

# humanKeypadTest = SmallKeypad(None, "debug2")
# numericKeypadTest = BigKeypad(humanKeypadTest)

# print(numericKeypadTest.find_shortest_path(*zero_position) + numericKeypadTest.find_shortest_path(*two_position) +
#       numericKeypadTest.find_shortest_path(*nine_position) + numericKeypadTest.find_shortest_path(*activate_position))