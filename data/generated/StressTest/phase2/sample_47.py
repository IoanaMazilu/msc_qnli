# Premise: Maddie has 24 apples, if she give 12 to mike, how many does she have left?
# Hypothesis: Maddie has 44 apples, if she give 12 to mike, how many does she have left?
# Golden Label: contradiction

apples_maddie_premise = 24
apples_given_premise = 12
apples_maddie_hypothesis = 44
apples_given_hypothesis = 12

# the hypothesis talks about the number of apples Maddie has and gives to Mike, which is also referenced in the premise
# first we check if the number of apples Maddie has in the hypothesis contradicts the number of apples she has in the premise
if apples_maddie_premise != apples_maddie_hypothesis:
    label = "contradiction"
# next, we check if the number of apples given to Mike in the hypothesis contradicts the number of apples given to Mike in the premise
elif apples_given_premise != apples_given_hypothesis:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

