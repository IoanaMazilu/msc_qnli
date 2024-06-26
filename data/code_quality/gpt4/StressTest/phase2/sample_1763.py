men_to_women_ratio_premise = 4/3
men_to_women_ratio_hypothesis = 4/3

# the hypothesis refers to the ratio of men to women in the choir, which is also mentioned in the premise
if men_to_women_ratio_hypothesis >= men_to_women_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis is less than the ratio in the premise, it doesn't contradict the premise, but it can't be explicitly entailed from it
    label = "neutral"

print(label)
