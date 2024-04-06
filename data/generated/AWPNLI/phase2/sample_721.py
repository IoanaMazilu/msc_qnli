# Premise: The farmer had 127.0 apples and his neighbor gave him 88.0 apples.
# Hypothesis: Farmer has 217.0 apples now.
# Golden Label: contradiction

apples_farmer_premise = 127.0
apples_from_neighbor_premise = 88.0
total_apples_hypothesis = 217.0

# the hypothesis refers to the total number of apples, which are also mentioned in the premise
# compute the total number of apples in the premise
total_apples_premise = apples_farmer_premise + apples_from_neighbor_premise
if total_apples_hypothesis != total_apples_premise:
    # check if the total number of apples in the hypothesis contradicts the total number of apples from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

