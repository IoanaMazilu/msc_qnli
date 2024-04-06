# Premise: Joan picked 43.0 apples from the orchard and Melanie gave Joan 27.0 more apples.
# Hypothesis: Joan has 74.0 apples now.
# Golden Label: contradiction

picked_apples_premise = 43.0
received_apples_premise = 27.0
total_apples_hypothesis = 74.0

# the hypothesis refers to the total number of apples, which are also mentioned in the premise
# compute the total number of apples in the premise
total_apples_premise = picked_apples_premise + received_apples_premise
if total_apples_hypothesis != total_apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

