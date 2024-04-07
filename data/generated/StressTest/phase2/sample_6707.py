# Premise: Yali builds a tower using only red, green, and blue toy bricks in a ratio of 4:3:1.
# Hypothesis: Yali builds a tower using only red, green, and blue toy bricks in a ratio of less than 4:3:1.
# Golden Label: contradiction

# ratios of red, green, and blue toy bricks in premise and hypothesis
red_green_blue_premise = (4, 3, 1)
red_green_blue_hypothesis = (4, 3, 1)

# since the hypothesis specifies a ratio less than 4:3:1, it should not be equal to 4:3:1
if red_green_blue_hypothesis == red_green_blue_premise:
    label = "contradiction"
else:
    # the premise doesn't give us any information about other possible ratios, so any ratio less than 4:3:1 is not contradicting the premise, but it can't be explicitly entailed from it
    label = "neutral"

print(label)

