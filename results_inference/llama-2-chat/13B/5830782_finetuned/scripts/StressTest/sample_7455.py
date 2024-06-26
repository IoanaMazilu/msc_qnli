apples_premise = 48
apples_given = 22
apples_hypothesis = 18

# the hypothesis refers to the number of apples Maddie has and gives to Mike, mentioned in the premise
if apples_given!= apples_premise:
    # check if the number of apples given in the hypothesis contradicts the number of apples given in the premise
    label = "contradiction"
elif apples_hypothesis >= apples_premise:
    # check if the estimate of 'apples_hypothesis' contradicts the number of apples Maddie has left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
