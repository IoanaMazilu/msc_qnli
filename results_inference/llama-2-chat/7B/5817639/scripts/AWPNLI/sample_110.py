apples_premise = 9.0
erasers_premise = 12.0
friends_premise = 3.0
apples_hypothesis = 3.0

# compare the number of apples in the hypothesis to the number of apples in the premise
if apples_hypothesis!= apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
