# Premise: Maddie has less than 34 apples, if she give 12 to mike, how many does she have left?
# Hypothesis: Maddie has 24 apples, if she give 12 to mike, how many does she have left?
# Golden Label: neutral

apples_maddie_premise = 34
apples_given_to_mike = 12
apples_maddie_hypothesis = 24

# the hypothesis refers to the number of apples Maddie has and the number she gives to Mike, both mentioned in the premise
if apples_maddie_hypothesis >= apples_maddie_premise:
    # check if the number of apples Maddie allegedly has in the hypothesis contradicts the premise estimate of less than 'apples_maddie_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

