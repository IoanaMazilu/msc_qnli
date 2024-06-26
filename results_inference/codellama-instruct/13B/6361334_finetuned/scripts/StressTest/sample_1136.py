shirt_premise = 1
shirt_hypothesis = 5
jeans_premise = 1
jeans_hypothesis = 1
sneakers_premise = 1
sneakers_hypothesis = 1

# the hypothesis refers to the number of shirts, jeans, and sneakers in an outfit
# the premise mentions the number of different outfits Jordan has
if shirt_hypothesis!= shirt_premise or jeans_hypothesis!= jeans_premise or sneakers_hypothesis!= sneakers_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise values
    # any number of outfits greater than or equal to 1 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
