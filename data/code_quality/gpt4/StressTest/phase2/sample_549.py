savings_premise = 32
savings_hypothesis = 42

# the hypothesis refers to the percentage of monthly salary Aamir saves, which is also mentioned in the premise
if savings_premise >= savings_hypothesis:
    # check if the percentage of savings in the premise contradicts the less than 'savings_hypothesis' condition
    label = "contradiction"
elif savings_hypothesis != savings_premise:
    # check if the percentage of savings in the hypothesis contradicts the percentage of savings reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
