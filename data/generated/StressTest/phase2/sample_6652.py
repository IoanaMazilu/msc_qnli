# Premise: Maddie has less than 88 apples, if she give 12 to mike, how many does she have left?
# Hypothesis: Maddie has 18 apples, if she give 12 to mike, how many does she have left?
# Golden Label: neutral

apples_maddie_premise = 88
apples_maddie_hypothesis = 18
apples_to_mike = 12

# the hypothesis refers to the number of apples Maddie has and the number she gives to Mike, which are both mentioned in the premise
if apples_maddie_hypothesis >= apples_maddie_premise:
    # check if the number of apples Maddie has in the hypothesis contradicts the premise
    label = "contradiction"
elif (apples_maddie_hypothesis - apples_to_mike) != (apples_maddie_hypothesis - apples_to_mike):
    # check if the number of apples Maddie has left after giving some to Mike in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples less than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

