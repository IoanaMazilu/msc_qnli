apples_maddie_premise = 4
apples_given_premise = 2
apples_left_premise = apples_maddie_premise - apples_given_premise

apples_maddie_hypothesis = 7
apples_given_hypothesis = 2
apples_left_hypothesis = apples_maddie_hypothesis - apples_given_hypothesis

# the hypothesis refers to the number of apples Maddie has and gives to Mike, which is also mentioned in the premise
if apples_left_premise!= apples_left_hypothesis:
    # check if the number of apples left with Maddie in the hypothesis contradicts the number of apples left with Maddie in the premise
    label = "contradiction"
elif apples_maddie_hypothesis <= apples_maddie_premise:
    # check if the estimate of 'apples_maddie_hypothesis' contradicts the number of apples Maddie has in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
