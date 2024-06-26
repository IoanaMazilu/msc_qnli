sheep_to_horses_ratio_premise = 6/7
sheep_to_horses_ratio_hypothesis = 1/7

# the hypothesis talks about the ratio of sheep to horses, which is also mentioned in the premise
if sheep_to_horses_ratio_hypothesis!= sheep_to_horses_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratios are the same, it is a neutral relation
    label = "neutral"

print(label)
