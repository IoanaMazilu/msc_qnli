raised_premise = 350000
raised_hypothesis = 350000

# the hypothesis mentions the amount raised by the Jordan Thomas Foundation, which is also mentioned in the premise
if raised_hypothesis!= raised_premise:
    # check if the amount raised in the hypothesis contradicts the amount raised reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
