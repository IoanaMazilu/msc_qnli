# Premise: Tali builds a tower using only red, green, and blue toy bricks in a ratio of 4:3:1.
# Hypothesis: Tali builds a tower using only red, green, and blue toy bricks in a ratio of more than 1:3:1.
# Golden Label: entailment

red_green_blue_ratio_premise = (4, 3, 1)
red_green_blue_ratio_hypothesis = (1, 3, 1)

# the hypothesis refers to the ratio of red:green:blue toy bricks used by Tali in building a tower, as mentioned in the premise
if red_green_blue_ratio_hypothesis[0] >= red_green_blue_ratio_premise[0]:
    # check if the number of red bricks in the ratio provided in the hypothesis contradicts the number in the premise's ratio
    label = "contradiction"
else:
    # the premise gives a specific ratio for the toy bricks
    # any ratio that has less red bricks than 'red_green_blue_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

