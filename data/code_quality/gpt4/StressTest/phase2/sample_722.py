total_purses_premise = 9
gift_purses_premise = 3
total_purses_hypothesis = 4
gift_purses_hypothesis = 3

# the hypothesis refers to the total number of purses and the number of gift purses mentioned in the premise
remaining_purses_premise = total_purses_premise - gift_purses_premise
remaining_purses_hypothesis = total_purses_hypothesis - gift_purses_hypothesis

if gift_purses_hypothesis != gift_purses_premise:
    # check if the number of gift purses in the hypothesis contradicts the number of gift purses reported in the premise
    label = "contradiction"
elif remaining_purses_hypothesis != remaining_purses_premise:
    # check if the remaining number of purses in the hypothesis contradicts the remaining number of purses after gifting in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
