#use the function input() to ask what will be the temperature today and store into a variable
temp = float(input("what will be the temperature today?"))
if temp < 12:
    print("It's cold outside, you should wear a jacket.")
elif temp < 6:
    print("you should wear a pair of gloves")
elif temp < 10:
    print("you shlould wear a scraf")
elif temp < 8:
    print("you should wear a hat")
elif temp > 25:
    print("you should ware a sunglasses")