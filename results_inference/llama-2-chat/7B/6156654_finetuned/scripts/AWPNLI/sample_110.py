apples_premise = 9.0
erasers_premise = 12.0
friends_premise = 3.0

apples_hypothesis = 3.0

# the hypothesis refers to the number of apples each friend got, which is also mentioned in the premise
if apples_hypothesis!= apples_premise:
    # check if the number of apples each friend got in the hypothesis contradicts the number of apples each friend got in the premise
    label = "contradiction"
else:
    # if the number of apples each friend got in the hypothesis matches the number of apples each friend got in the premise, we can infer entailment
    label = "entailment"

print(label)
