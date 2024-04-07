# Premise: Maddie has 15 apples, if she give 8 to mike, how many does she have left?
# Hypothesis: Maddie has 75 apples, if she give 8 to mike, how many does she have left?
# Golden Label: contradiction

apples_maddie_premise = 15
apples_maddie_hypothesis = 75
apples_given = 8

# the hypothesis refers to the number of apples Maddie initially had, which is also mentioned in the premise
if apples_maddie_premise != apples_maddie_hypothesis:
    # check if the number of apples Maddie initially had in the hypothesis contradicts the number of apples Maddie initially had reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

