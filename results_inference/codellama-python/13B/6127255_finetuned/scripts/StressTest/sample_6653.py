apples_maddie_premise = 18
apples_maddie_hypothesis = 58
apples_given_premise = 12
apples_given_hypothesis = 12

# the hypothesis talks about the number of apples Maddie has and gives to Mike, referenced also in the premise
if apples_given_hypothesis!= apples_given_premise:
    # check if the number of apples given in the hypothesis contradicts the number of apples given reported in the premise
    label = "contradiction"
elif apples_maddie_hypothesis!= apples_maddie_premise:
    # check if the number of apples Maddie has in the hypothesis contradicts the number of apples Maddie has reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
