total_purses_premise = 14
gift_purses_premise = 3
total_purses_hypothesis = 34
gift_purses_hypothesis = 3

# the hypothesis refers to the total number of purses and the number of purses given as gift mentioned in the premise
if total_purses_premise - gift_purses_premise!= total_purses_hypothesis - gift_purses_hypothesis:
    # check if the difference between the total number of purses and the number of gift purses in the hypothesis contradicts the same difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
