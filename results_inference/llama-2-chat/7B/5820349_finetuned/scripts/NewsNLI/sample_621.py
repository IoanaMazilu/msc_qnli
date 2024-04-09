chance_arrested_premise = 0.4
chance_arrested_hypothesis = 0.4

# the hypothesis mentions the chance of arrest for white males, which is also referenced in the premise
if chance_arrested_hypothesis!= chance_arrested_premise:
    # check if the chance of arrest in the hypothesis contradicts the chance of arrest reported in the premise
    label = "contradiction"
else:
    # if the chance of arrest in the hypothesis does not contradict the chance of arrest in the premise, we can infer entailment
    label = "entailment"

print(label)
