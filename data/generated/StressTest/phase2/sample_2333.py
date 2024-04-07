# Premise: Christine and Siri have 21 rs between them.
# Hypothesis: Christine and Siri have 51 rs between them.
# Golden Label: contradiction

rs_premise = 21
rs_hypothesis = 51

# the hypothesis refers to the amount of rs Christine and Siri have, also mentioned in the premise
if rs_hypothesis != rs_premise:
    # check if the number of rs in the hypothesis contradicts the number of rs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

