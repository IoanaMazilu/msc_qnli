suresh_efficiency_premise = 25
suresh_efficiency_hypothesis = 35

# the hypothesis refers to the efficiency of Suresh compared to Kamal mentioned in the premise
if suresh_efficiency_hypothesis < suresh_efficiency_premise:
    # check if the hypothesis value contradicts the efficiency difference in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
