red_green_blue_ratio_premise = 3/3/1
red_green_blue_ratio_hypothesis = 4/3/1

# the hypothesis talks about the ratio of red, green and blue toy bricks used in building the tower, referenced also in the premise
if red_green_blue_ratio_hypothesis <= red_green_blue_ratio_premise:
    # check if the hypothesis ratio contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
