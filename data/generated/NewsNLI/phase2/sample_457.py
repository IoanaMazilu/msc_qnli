# Premise: For that, six protesters and counterprotesters got themselves arrested, Murrieta police said.
# Hypothesis: Six protesters and counterprotesters were arrested.
# Golden Label: entailment

arrested_premise = 6
arrested_hypothesis = 6

# the hypothesis mentions the number of arrested protesters, which is also referenced in the premise
if arrested_hypothesis != arrested_premise:
    # check if the number of arrested protesters in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of arrested protesters in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

