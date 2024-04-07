# Premise: Caleb spends $74.50 on 50 hamburgers for the marching band.
# Hypothesis: Caleb spends $74.50 on 60 hamburgers for the marching band.
# Golden Label: contradiction

spend_premise = 74.50
hamburgers_premise = 50
hamburgers_hypothesis = 60

# the hypothesis talks about the spending and number of hamburgers, both mentioned in the premise
if hamburgers_hypothesis != hamburgers_premise:
    # check if the number of hamburgers in the hypothesis contradicts the number of hamburgers in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

