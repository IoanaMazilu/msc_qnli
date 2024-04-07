# Premise: If there are 1500 hunters in Piscataquis County then how many fishermen are there?
# Hypothesis: If there are less than 1500 hunters in Piscataquis County then how many fishermen are there?
# Golden Label: contradiction

hunters_premise = 1500
hunters_hypothesis = 1500

# the hypothesis refers to the number of hunters mentioned in the premise
if hunters_hypothesis >= hunters_premise:
    # check if the estimate of 'hunters_hypothesis' contradicts the number of hunters in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

