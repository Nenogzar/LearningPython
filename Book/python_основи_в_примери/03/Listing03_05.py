Alpha = 5 * [0]
print(f"Alpha=5*[0] => {Alpha}")
Bravo = (1,) * 3
print(f"Bravo=(1,)*3 => {Bravo}")

Charlie = [1, 2] * 3
print(f"Charlie=[1,2]*3 => {Charlie}")

Delta = [[1, 2]] * 3
print(f"Delta=[[1,2]]*3 => {Delta}")

Echo = 4 * (1, [2, 3])
print(f"Echo=4*(1,[2,3]) => {Echo}")

Foxtrot = ([1] * 2) * 3
print(f"Foxtrot=([1]*2)*3 {Foxtrot}")

Golf = ([1] * 2,) * 3
print(f"Golf=([1]*2,)*3 => {Golf}")
