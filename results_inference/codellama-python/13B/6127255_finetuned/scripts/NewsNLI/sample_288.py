injured_premise = 1500
unsheltered_premise = 50000
unsheltered_hypothesis = 50000

# the hypothesis mentions the number of people without shelter, which is also mentioned in the premise
if unsheltered_hypothesis!= unsheltered_premise:
    # check if the number of unsheltered people in the hypothesis contradicts the number of unsheltered people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
