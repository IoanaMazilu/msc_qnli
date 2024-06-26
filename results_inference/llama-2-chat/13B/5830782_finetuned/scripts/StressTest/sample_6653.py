apples_maddie_premise = 18
apples_given_premise = 12
apples_maddie_left_premise = apples_maddie_premise - apples_given_premise

apples_maddie_hypothesis = 58
apples_given_hypothesis = 12
apples_maddie_left_hypothesis = apples_maddie_hypothesis - apples_given_hypothesis

# the hypothesis talks about the number of apples Maddie had, the number of apples she gave to Mike, and the number of apples she had left after giving those to Mike
if apples_maddie_premise!= apples_maddie_hypothesis:
    # check if the number of apples Maddie had in the hypothesis contradicts the number of apples Maddie had in the premise
    label = "contradiction"
elif apples_given_premise!= apples_given_hypothesis:
    # check if the number of apples given to Mike in the hypothesis contradicts the number of apples given to Mike in the premise
    label = "contradiction"
elif apples_maddie_left_premise!= apples_maddie_left_hypothesis:
    # check if the number of apples Maddie had left after giving to Mike in the hypothesis contradicts the number of apples Maddie had left after giving to Mike in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
