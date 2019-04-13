def band_name_generator(name):
    if name[0] == name[len(name)-1]:
        return name.capitalize() + name[1:]
    else:
        return "The " + name.capitalize() 