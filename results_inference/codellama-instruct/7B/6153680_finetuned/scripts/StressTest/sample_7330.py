red_ratio = 4
green_ratio = 3
blue_ratio = 1

# the hypothesis refers to the ratio of red, green, and blue bricks used in the tower
if red_ratio > 3 and green_ratio > 3 and blue_ratio == 1:
    # check if the hypothesis values contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
