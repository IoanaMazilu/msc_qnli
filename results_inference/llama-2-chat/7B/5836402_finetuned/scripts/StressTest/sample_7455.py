apples_initial_premise = 48
apples_given_premise = 22
apples_left_premise = apples_initial_premise - apples_given_premise
apples_hypothesis = 18

# the hypothesis refers to the number of apples Maddie has left, which is also mentioned in the premise
if apples_hypothesis <= apples_left_premise:
    # check if the hypothesis value contradicts the number of apples left in the premise
    label = "contradiction"
elif apples_hypothesis > apples_left_premise:
    # check if the number of apples in the hypothesis is greater than the number of apples left in the premise
    # this is possible and consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
