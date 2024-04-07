# Premise: Maddie has 4 apples, if she give 2 to mike, how many does she have left?
# Hypothesis: Maddie has 6 apples, if she give 2 to mike, how many does she have left?
# Golden Label: contradiction

apples_maddie_premise = 4
apples_given_to_mike = 2
apples_maddie_hypothesis = 6

# the hypothesis refers to the number of apples Maddie has, similar to the premise
if apples_maddie_premise != apples_maddie_hypothesis:
    # check if the number of apples Maddie has in the hypothesis contradicts the number of apples Maddie has in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

