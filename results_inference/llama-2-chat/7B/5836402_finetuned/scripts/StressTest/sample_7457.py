apples_maddie_premise = 48
apples_given_premise = 22
apples_left_premise = apples_maddie_premise - apples_given_premise

apples_maddie_hypothesis = 88
apples_given_hypothesis = 22
apples_left_hypothesis = apples_maddie_hypothesis - apples_given_hypothesis

# the hypothesis refers to the number of apples Maddie has and gives away, as well as the number of apples she has left
if apples_left_hypothesis!= apples_left_premise:
    # check if the number of apples Maddie has left in the hypothesis contradicts the number of apples she has left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
