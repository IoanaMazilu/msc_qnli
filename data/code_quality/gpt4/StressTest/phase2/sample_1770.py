gang_count_premise = 9
gang_count_hypothesis = 1

# the hypothesis talks about the number of friendship gangs Raja has, which is also referenced in the premise
if gang_count_hypothesis >= gang_count_premise:
    # check if the hypothesis value contradicts the number of friendship gangs in the premise
    label = "contradiction"
elif gang_count_hypothesis < gang_count_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)