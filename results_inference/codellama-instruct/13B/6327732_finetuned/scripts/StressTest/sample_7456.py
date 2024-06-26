apples_maddie_premise = 18
apples_maddie_hypothesis = 48
apples_mike_premise = 22
apples_mike_hypothesis = 22

# the hypothesis refers to the number of apples Maddie has and the number of apples she gives to Mike
if apples_maddie_hypothesis <= apples_maddie_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_maddie_premise'
    label = "contradiction"
elif apples_mike_hypothesis!= apples_mike_premise:
    # check if the number of apples given to Mike in the hypothesis contradicts the number of apples given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
