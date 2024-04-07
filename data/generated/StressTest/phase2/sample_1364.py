# Premise: Maddie has 6 apples, if she give 3 to mike, how many does she have left?
# Hypothesis: Maddie has more than 6 apples, if she give 3 to mike, how many does she have left?
# Golden Label: contradiction

apples_maddie_premise = 6
apples_maddie_hypothesis = 6
apples_given_mike = 3

# the hypothesis refers to the number of apples that Maddie has and is giving to Mike mentioned in the premise
if apples_maddie_hypothesis != apples_maddie_premise:
    # check if the number of apples Maddie has in the hypothesis contradicts the number of apples Maddie has in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

