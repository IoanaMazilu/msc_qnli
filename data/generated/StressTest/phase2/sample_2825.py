# Premise: Caleb spends $66.50 on 50 hamburgers for the marching band.
# Hypothesis: Caleb spends $66.50 on 80 hamburgers for the marching band.
# Golden Label: contradiction

spend_on_hamburgers_premise = 66.50
hamburgers_premise = 50
spend_on_hamburgers_hypothesis = 66.50
hamburgers_hypothesis = 80

# the hypothesis refers to the number of hamburgers bought by Caleb and the money spent, mentioned in the premise
if hamburgers_hypothesis != hamburgers_premise:
    # check if the number of hamburgers in the hypothesis contradicts the number of hamburgers reported in the premise
    label = "contradiction"
elif spend_on_hamburgers_hypothesis != spend_on_hamburgers_premise:
    # check if the money spent on hamburgers in the hypothesis contradicts the money spent on hamburgers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

