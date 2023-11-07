import sys
#from fizzbuzz_function import fizzbuzz

count = int(sys.argv[2])
string1 = sys.argv[3]
string2 = sys.argv[4]
string3 = sys.argv[5]

if sys.argv[1] == "0":
    fizzbuzz()
elif sys.argv[1] == "1":
    fizzbuzz(count)
elif sys.argv[1] == "2":
    fizzbuzz(count, string1)
elif sys.argv[1] == "3":
    fizzbuzz(count, string1, string2)
elif sys.argv[1] == "4":
    fizzbuzz(count, string1, string2, string3)
elif sys.argv[1] == "5":
    fizzbuzz(buzz=string1, fizzbuzz=string2, fizz=string3, count=count)
