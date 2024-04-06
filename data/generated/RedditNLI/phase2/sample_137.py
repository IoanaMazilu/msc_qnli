# Premise: 4 banks become first to repay government aid.
# Hypothesis: 4 Regional Banks Are the First to Repay Government Aid.
# Golden Label: neutral

banks_premise = 4
banks_hypothesis = 4

# the hypothesis and premise mention the number of banks that were first to repay government aid
if banks_hypothesis != banks_premise:
    # check if the number of banks in the hypothesis contradicts the number of banks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

