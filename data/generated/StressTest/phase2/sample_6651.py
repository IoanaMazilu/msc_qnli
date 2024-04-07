# Premise: Maddie has 18 apples, if she give 12 to mike, how many does she have left?
# Hypothesis: Maddie has less than 88 apples, if she give 12 to mike, how many does she have left?
# Golden Label: entailment

apples_maddie_premise = 18
apples_given_to_mike_premise = 12
apples_maddie_hypothesis = 88
apples_given_to_mike_hypothesis = 12

# the hypothesis refers to the number of apples Maddie has and the number of apples she gives to Mike, mentioned in the premise
if apples_maddie_hypothesis <= apples_maddie_premise:
    # check if the estimate of 'apples_maddie_hypothesis' contradicts the number of apples Maddie has in the premise
    label = "contradiction"
elif apples_given_to_mike_hypothesis != apples_given_to_mike_premise:
    # check if the number of apples given to Mike in the hypothesis contradicts the number of apples given to Mike in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

