# Premise: The last four cars went off the track, the railway company said.
# Hypothesis: Last four cars of train derailed, the railway company says.
# Golden Label: entailment

cars_premise = 4
cars_hypothesis = 4

# the hypothesis mentions the number of cars that derailed which is also mentioned in the premise
if cars_hypothesis != cars_premise:
    # check if the number of cars in the hypothesis contradicts the number of cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

