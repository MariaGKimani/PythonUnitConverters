def gram_to_ounces(grams):
    ounces = grams * 0.03527
    return ounces

grams = float(input("Enter weight in grams:"))
ounces = gram_to_ounces(grams)
print (f" The weightin ounces is: {ounces} oz")