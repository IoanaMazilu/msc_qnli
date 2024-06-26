apples_premise = 48
apples_hypothesis = 18
apples_given_premise = 22
apples_given_hypothesis = 22

# the hypothesis talks about the number of apples Maddie has and gives an estimate for the number of apples she gives to Mike
if apples_hypothesis <= apples_premise:
    # check if the hypothesis estimate contradicts the number of apples in the premise
    label = "contradiction"
elif apples_given_hypothesis!= apples_given_premise:
    # check if the number of apples given in the hypothesis contradicts the number of apples given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
