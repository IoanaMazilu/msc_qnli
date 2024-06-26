apples_premise = 88
apples_hypothesis = 18
apples_given_premise = 12
apples_given_hypothesis = 12

# the hypothesis refers to the number of apples Maddie has and gives to Mike, as mentioned in the premise
if apples_hypothesis <= apples_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_premise'
    label = "contradiction"
elif apples_given_hypothesis!= apples_given_premise:
    # check if the number of apples given in the hypothesis contradicts the number of apples given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
