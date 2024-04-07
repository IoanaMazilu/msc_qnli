# Premise: If it takes Darcy a total of more than 2 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Hypothesis: If it takes Darcy a total of 5 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Golden Label: neutral

commute_diff_premise = 2
commute_diff_hypothesis = 5

# the hypothesis refers to the same difference in commuting time mentioned in the premise
if commute_diff_hypothesis <= commute_diff_premise:
    # check if the hypothesis value contradicts the estimate of more than 'commute_diff_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference in commuting time
    # any difference in commuting time greater than 'commute_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

