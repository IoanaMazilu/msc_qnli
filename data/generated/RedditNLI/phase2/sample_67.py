# Premise: Fed's Rosengren Wants Two More Hikes in 2018 as Economy Grows.
# Hypothesis: Top Fed official wants two more rate hikes in 2018 as US economy grows.
# Golden Label: entailment

hikes_premise = 2
hikes_hypothesis = 2

# the hypothesis and premise mention the number of hikes in 2018
if hikes_hypothesis != hikes_premise:
    # check if the number of hikes in the hypothesis contradicts the number of hikes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
