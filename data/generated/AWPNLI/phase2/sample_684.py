# Premise: Maria has 45.0 bottles of water in her fridge, and she drank 14.0 of them and her sister drank 8.0.
# Hypothesis: 23.0 bottles are left.
# Golden Label: entailment

initial_bottles_premise = 45.0
drank_maria_premise = 14.0
drank_sister_premise = 8.0
left_bottles_hypothesis = 23.0

# the hypothesis refers to the number of bottles left, which is also referenced in the premise
# calculate the number of bottles left in the premise
left_bottles_premise = initial_bottles_premise - drank_maria_premise - drank_sister_premise
if left_bottles_hypothesis != left_bottles_premise:
    # check if the number of bottles left in the hypothesis contradicts the number of bottles left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

