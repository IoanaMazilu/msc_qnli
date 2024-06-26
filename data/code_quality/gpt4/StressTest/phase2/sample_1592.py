share_sravan_premise = 5535
share_sravan_hypothesis = 3535

# the hypothesis refers to the share of Sravan mentioned in the premise
if share_sravan_hypothesis != share_sravan_premise:
    # check if the share of Sravan in the hypothesis contradicts the share of Sravan mentioned in the premise
    label = "contradiction"
else:
    # if the share of Sravan in the hypothesis does not contradict the share of Sravan in the premise, we can infer entailment
    label = "entailment"

print(label)
