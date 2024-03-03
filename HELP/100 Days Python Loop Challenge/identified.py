identified =['Bird', 'Plane', 'Superman', 'Koko']

def login(observed):
    for item in identified:
        if observed.lower() == item.lower():
            return observed
    return "Does not mean i visit of ann extraterrestrial."

print(login("UFO"))

