commute_walk_premise = 55
commute_walk_hypothesis = 15

# the hypothesis refers to the number of minutes Darcy needs to commute to work by walking, referenced also in the premise
if commute_walk_hypothesis >= commute_walk_premise:
    # check if the hypothesis value contradicts the estimate of less than 'commute_walk_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of minutes Darcy needs to commute to work by walking
    # any number of minutes less than 'commute_walk_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
