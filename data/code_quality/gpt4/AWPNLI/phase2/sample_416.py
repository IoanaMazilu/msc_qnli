picked_apples_premise = 43.0
received_apples_premise = 27.0
total_apples_hypothesis = 70.0

# the hypothesis refers to the total number of apples Joan has now, which is also calculated in the premise
# compute the total number of apples in the premise
total_apples_premise = picked_apples_premise + received_apples_premise
if total_apples_hypothesis != total_apples_premise:
    # check if the total number of apples in the hypothesis contradicts the total number of apples from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
