superstars_beaches_premise = 35
superstars_beaches_hypothesis = 35

# the hypothesis mentions the number of 'superstar' beaches, which is also mentioned in the premise
if superstars_beaches_hypothesis != superstars_beaches_premise:
    # check if the number of 'superstar' beaches in the hypothesis contradicts the number stated in the premise
    label = "contradiction"
else:
    # if the number of 'superstar' beaches in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
