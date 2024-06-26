bottles_premise = 45.0
drunk_premise = 14.0
sister_drunk_premise = 8.0
left_hypothesis = 23.0

# compute the total amount of water left in the fridge
total_left = bottles_premise - (drunk_premise + sister_drunk_premise)

if left_hypothesis > total_left:
    # check if the number of bottles left in the hypothesis contradicts the estimate of total water left in the premise
    label = "contradiction"
elif left_hypothesis == total_left:
    # if the hypothesis value and the estimate of total water left in the premise are equal, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value and the estimate of total water left in the premise do not contradict, we can infer entailment
    label = "entailment"

print(label)
