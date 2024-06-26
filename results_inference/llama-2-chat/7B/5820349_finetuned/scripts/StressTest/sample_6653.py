apples_maddie_premise = 18
apples_given_premise = 12
apples_maddie_hypothesis = 58
apples_given_hypothesis = 12

# the hypothesis refers to the number of apples Maddie has and gives to Mike, mentioned in the premise
if apples_maddie_premise!= apples_maddie_hypothesis:
    # check if the number of apples Maddie has in the hypothesis contradicts the number of apples she has in the premise
    label = "contradiction"
elif apples_given_premise!= apples_given_hypothesis:
    # check if the number of apples Maddie gives to Mike in the hypothesis contradicts the number of apples she gives to Mike in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
