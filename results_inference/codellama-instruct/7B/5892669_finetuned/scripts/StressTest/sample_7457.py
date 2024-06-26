apples_maddie_premise = 48
apples_maddie_hypothesis = 88
apples_given_premise = 22
apples_given_hypothesis = 22

# the hypothesis refers to the number of apples Maddie has and the number of apples she gives to Mike, mentioned in the premise
if apples_maddie_premise!= apples_maddie_hypothesis:
    # check if the number of apples Maddie has in the hypothesis contradicts the number of apples Maddie has in the premise
    label = "contradiction"
elif apples_given_premise!= apples_given_hypothesis:
    # check if the number of apples given to Mike in the hypothesis contradicts the number of apples given to Mike in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
