apples_premise = 48
apples_hypothesis = 18
given_apples_premise = 22
given_apples_hypothesis = 22

# the hypothesis refers to the number of apples Maddie has after giving some to Mike
if apples_hypothesis < apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples in the premise
    label = "contradiction"
elif given_apples_hypothesis!= given_apples_premise:
    # check if the number of apples Maddie gives to Mike in the hypothesis contradicts the number of apples Maddie gives to Mike in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
