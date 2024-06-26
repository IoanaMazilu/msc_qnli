loyalty_scheme_premise = 40
loyalty_scheme_hypothesis = 40

# the hypothesis mentions the percentage of passengers who never redeem loyalty miles, which is also mentioned in the premise
if loyalty_scheme_hypothesis!= loyalty_scheme_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
