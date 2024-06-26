shirt_outfit_premise = 1
jeans_outfit_premise = 1
sneakers_outfit_premise = 1

shirt_outfit_hypothesis = 5
jeans_outfit_hypothesis = 1
sneakers_outfit_hypothesis = 1

# the hypothesis refers to the number of shirts, jeans, and sneakers in an outfit
if shirt_outfit_hypothesis <= shirt_outfit_premise and jeans_outfit_hypothesis <= jeans_outfit_premise and sneakers_outfit_hypothesis <= sneakers_outfit_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts, jeans, and sneakers in an outfit
    # any number of shirts, jeans, and sneakers greater than the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
