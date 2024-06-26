# Defining the ratio for each color in the premise and hypothesis
red_green_blue_premise = (4, 3, 1)
red_green_blue_hypothesis = (4, 3, 1)

# The hypothesis refers to the ratio of colors of bricks used by Lali as stated in the premise
if red_green_blue_hypothesis <= red_green_blue_premise:
    # If the ratio in the hypothesis is less than or equal to the ratio in the premise,
    # then it contradicts the premise which states that the ratio is more than 4:3:1
    label = "contradiction"
else:
    # The premise gives only an estimate for the ratio of the bricks
    # Any ratio that is more than 4:3:1 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
