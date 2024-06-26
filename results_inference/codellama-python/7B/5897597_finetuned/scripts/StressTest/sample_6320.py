apples_maddie_premise = 4
apples_maddie_hypothesis = 6
apples_given = 2

# the hypothesis refers to the number of apples Maddie initially had, which is also mentioned in the premise
if apples_maddie_premise!= apples_maddie_hypothesis:
    # check if the number of apples Maddie initially had in the hypothesis contradicts the number of apples mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
