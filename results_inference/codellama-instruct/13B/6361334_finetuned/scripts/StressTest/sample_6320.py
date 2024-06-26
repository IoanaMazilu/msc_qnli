apples_maddie_premise = 4
apples_maddie_hypothesis = 6

# the hypothesis refers to the number of apples Maddie has after giving 2 to Mike
# the premise mentions the number of apples Maddie has before giving any to Mike
if apples_maddie_hypothesis!= apples_maddie_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples in the premise
    label = "contradiction"
else:
    # if the number of apples in the hypothesis is consistent with the number of apples in the premise, we can infer entailment
    label = "entailment"

print(label)
