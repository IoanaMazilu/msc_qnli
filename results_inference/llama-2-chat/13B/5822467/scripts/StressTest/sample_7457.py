apples_premise = 48
apples_hypothesis = 88

# the hypothesis refers to the number of apples Maddie has after giving some to Mike
if apples_hypothesis <= apples_premise:
    # check if the estimate of 'apples_hypothesis' contradicts the number of apples Maddie has reported in the premise
    label = "contradiction"
elif apples_premise - 22 == apples_hypothesis - 22:
    # check if the number of apples Maddie has after giving 22 to Mike in the hypothesis contradicts the number of apples Maddie has after giving 22 to Mike in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
