a = int(input("a :"))
b = int(input("b :"))


print(f"{a if a < b else b} is Smaler")


time_strings = [f"{h}:{m}" for h in range(24) for m in range(60)]
#print(time_strings) # ['0:0', '0:1', '0:2', '0:3', '0:4', '0:5', ...
[print(time) for time in time_strings]  # 0:0
                                        # 0:1
                                        # ...
                                        # 23:58
                                        # 23:59



