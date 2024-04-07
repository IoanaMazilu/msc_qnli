# Premise: Maddie has 48 apples, if she give 22 to mike, how many does she have left?
# Hypothesis: Maddie has more than 18 apples, if she give 22 to mike, how many does she have left?
# Golden Label: entailment

apples_maddie_premise = 48
apples_given_to_mike_premise = 22
apples_maddie_hypothesis = 18
apples_given_to_mike_hypothesis = 22

# the hypothesis refers to the number of apples Maddie has and gives to Mike, mentioned in the premise
if apples_maddie_hypothesis >= apples_maddie_premise - apples_given_to_mike_premise:
    # check if the hypothesis value contradicts the premise on the number of apples Maddie has after giving some to Mike
    label = "contradiction"
elif apples_given_to_mike_hypothesis != apples_given_to_mike_premise:
    # check if the number of apples given to Mike in the hypothesis contradicts the number of apples given to Mike in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

