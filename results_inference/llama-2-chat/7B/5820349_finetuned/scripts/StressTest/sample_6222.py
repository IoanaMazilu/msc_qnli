share_difference_premise = 200
share_difference_hypothesis = 400

# the hypothesis refers to the difference between Mani and Rani's share mentioned in the premise
if share_difference_premise >= share_difference_hypothesis:
    # check if the estimate of'share_difference_hypothesis' contradicts the number of share difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
