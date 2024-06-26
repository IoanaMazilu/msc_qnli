shirt_outfit = 1
jeans_outfit = 1
sneakers_outfit = 1

# the hypothesis refers to the number of shirts, jeans, and sneakers in an outfit
if shirt_outfit < 4 and jeans_outfit == 1 and sneakers_outfit == 1:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of outfits
    # any number of outfits greater than'shirt_outfit' contradicts the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
