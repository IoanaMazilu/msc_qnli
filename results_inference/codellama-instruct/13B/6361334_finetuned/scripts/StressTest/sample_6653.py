apples_maddie_premise = 18
apples_mike_premise = 12
apples_maddie_hypothesis = 58
apples_mike_hypothesis = 12

# the hypothesis refers to the number of apples Maddie has and the number of apples she gives to Mike
# the premise also talks about the number of apples Maddie has and the number of apples she gives to Mike
if apples_maddie_hypothesis!= apples_maddie_premise:
    # check if the number of apples Maddie has in the hypothesis contradicts the number of apples she has in the premise
    label = "contradiction"
elif apples_mike_hypothesis!= apples_mike_premise:
    # check if the number of apples Mike gets in the hypothesis contradicts the number of apples he gets in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
