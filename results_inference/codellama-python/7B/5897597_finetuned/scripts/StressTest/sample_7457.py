apples_maddie_premise = 48
apples_maddie_hypothesis = 88
apples_given = 22

# the hypothesis refers to the number of apples Maddie initially had, which is also mentioned in the premise
if apples_maddie_hypothesis!= apples_maddie_premise:
    # check if the number of apples Maddie initially had in the hypothesis contradicts the number of apples mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
