apples_maddie_premise = 4
apples_maddie_hypothesis = 6
apples_given_premise = 2
apples_given_hypothesis = 2

# the hypothesis talks about the number of apples Maddie has and gives to Mike, referenced also in the premise
if apples_maddie_premise!= apples_maddie_hypothesis:
    # check if the number of apples Maddie has in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif apples_given_premise!= apples_given_hypothesis:
    # check if the number of apples Maddie gives to Mike in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
