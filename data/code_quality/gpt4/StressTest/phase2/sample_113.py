cleaning_time_premise = 4
cleaning_time_hypothesis = 6

# the hypothesis refers to the time Bruce and Anne need to clean the house, mentioned also in the premise
if cleaning_time_hypothesis != cleaning_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the time values in the hypothesis and premise match, we can infer entailment
    label = "entailment"

print(label)
