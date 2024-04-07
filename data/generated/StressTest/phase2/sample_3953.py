# Premise: 6970, then what will be the share of Sameer in the profit?
# Hypothesis: more than 6970, then what will be the share of Sameer in the profit?
# Golden Label: contradiction

sameer_share_premise = 6970
sameer_share_hypothesis = 6970

# the hypothesis refers to the share of Sameer mentioned in the premise
if sameer_share_hypothesis != sameer_share_premise:
    # check if the value of 'sameer_share_hypothesis' contradicts the share of Sameer in the premise
    label = "contradiction"
elif sameer_share_hypothesis <= sameer_share_premise:
    # check if the hypothesis value contradicts the estimate of more than 'sameer_share_premise'
    label = "contradiction"
else:
    # the premise gives exactly the share of Sameer
    # any share equal to 'sameer_share_premise' is consistent with the premise, can be explicitly entailed from the premise
    label = "entailment"

print(label)

