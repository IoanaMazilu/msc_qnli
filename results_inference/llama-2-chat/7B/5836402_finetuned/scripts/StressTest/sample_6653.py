apples_maddie_premise = 18
apples_given_premise = 12
apples_maddie_hypothesis = 58
apples_given_hypothesis = 12

# the hypothesis refers to the number of apples Maddie has and the number of apples she gave, both mentioned in the premise
if apples_maddie_premise!= apples_maddie_hypothesis:
    # check if the number of apples Maddie has in the hypothesis contradicts the number of apples from the premise
    label = "contradiction"
elif apples_given_hypothesis!= apples_given_premise:
    # check if the number of apples Maddie gave in the hypothesis contradicts the number of appies Maddie gave in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
