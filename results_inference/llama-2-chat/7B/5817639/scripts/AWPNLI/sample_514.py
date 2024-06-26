birds_premise = float(4.0)
birds_hypothesis = float(2.0)

# compare the number of birds in the premise and hypothesis
if birds_premise >= birds_hypothesis:
    # check if the number of birds in the hypothesis contradicts the estimate from the premise
    label = "contradiction"
elif birds_hypothesis!= birds_premise:
    # if the number of birds in the hypothesis does not contradict the estimate from the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
