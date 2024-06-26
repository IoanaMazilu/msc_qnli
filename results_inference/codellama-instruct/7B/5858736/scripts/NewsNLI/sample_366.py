guns_premise = 10
guns_hypothesis = 10

# the hypothesis mentions at least 10 shots, which is also mentioned in the premise
if guns_hypothesis!= guns_premise:
    # check if the number of shots in the hypothesis contradicts the number of shots in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
