# Premise: I am the single mother of three sons -- grown to manhood and doing just fine.
# Hypothesis: Weldon says she's a single mom of three flourishing young men, productive and happy.
# Golden Label: entailment

sons_premise = 3
sons_hypothesis = 3

# the hypothesis mentions the number of sons the woman has, which is also referenced in the premise
if sons_hypothesis != sons_premise:
    # check if the number of sons in the hypothesis contradicts the number of sons in the premise
    label = "contradiction"
else:
    # if the number of sons in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

