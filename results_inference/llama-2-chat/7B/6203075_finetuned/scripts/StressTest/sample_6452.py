# The hypothesis refers to the same situation as the premise, but with a different percentage of passengers from North America

# The hypothesis states that less than 1/12 of the passengers are from North America, which is also mentioned in the premise
if (1/12) / 100 < (1/12) / 100:
    # check if the ratio of passengers from North America in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratios are the same, we can infer entailment
    label = "entailment"

print(label)
