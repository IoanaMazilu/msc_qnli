total_purses_premise = 8
gift_purses_premise = 3
total_purses_hypothesis = 4
gift_purses_hypothesis = 3

# the hypothesis refers to the number of total purses and gift purses mentioned in the premise
if gift_purses_hypothesis!= gift_purses_premise:
    # check if the number of gift purses in the hypothesis contradicts the number of gift purses reported in the premise
    label = "contradiction"
elif total_purses_hypothesis!= (total_purses_premise - gift_purses_premise):
    # check if the number of total purses in the hypothesis contradicts the number of total purses after giving gifts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
