picked_apples_premise = 2.0
picked_apples_hypothesis = 10.0

# the hypothesis refers to the total number of apples picked, which is also mentioned in the premise
total_picked_apples_premise = picked_apples_premise + picked_apples_hypothesis

if picked_apples_hypothesis > total_picked_apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples from the premise
    label = "contradiction"
elif picked_apples_hypothesis == total_picked_apples_premise:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
