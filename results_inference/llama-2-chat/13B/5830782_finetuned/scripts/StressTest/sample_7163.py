red_green_blue_premise = [4, 3, 1]
red_green_blue_hypothesis = [4, 3, 1]

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Gali to build a tower
if red_green_blue_hypothesis >= red_green_blue_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
