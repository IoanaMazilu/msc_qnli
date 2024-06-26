people_trapped_premise_min = 20
people_trapped_premise_max = 30
people_trapped_hypothesis_max = 30

# the hypothesis mentions the maximum number of people thought trapped in the casino, which is also referenced in the premise
if people_trapped_hypothesis_max < people_trapped_premise_min or people_trapped_hypothesis_max > people_trapped_premise_max:
    # check if the maximum number of people trapped in the hypothesis contradicts the minimum and maximum number of people trapped reported in the premise
    label = "contradiction"
else:
    # if the maximum number of people trapped in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
