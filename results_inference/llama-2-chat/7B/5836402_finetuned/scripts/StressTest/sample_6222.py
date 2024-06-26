share_difference_premise = 200
share_difference_hypothesis = 400

# the hypothesis refers to the difference in shares between Mani and Rani, which is also mentioned in the premise
if share_difference_hypothesis >= share_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than'share_difference_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
