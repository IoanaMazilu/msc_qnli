# Premise: Maddie has 48 apples, if she give 22 to mike, how many does she have left?
# Hypothesis: Maddie has 88 apples, if she give 22 to mike, how many does she have left?
# Golden Label: contradiction

apples_maddie_premise = 48
apples_maddie_hypothesis = 88
apples_given_to_mike = 22

# the hypothesis talks about the number of apples Maddie has, referenced also in the premise
if apples_maddie_hypothesis != apples_maddie_premise:
    # check if the number of apples Maddie has in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif apples_given_to_mike != 22:
    # check if the number of apples given to Mike contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

