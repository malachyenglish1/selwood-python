def cels_convert(cels_temp):
     fahr_temp = cels_temp * 9/5 + 32
     print(f"{cels_temp} degrees C = ", fahr_temp, " degrees F")
     return

def fahr_convert(fahr_temp):
    cels_temp = (fahr_temp - 32) * 5/9
    print(f"{fahr_temp} degrees F = ", cels_temp, " degrees C")
    return
