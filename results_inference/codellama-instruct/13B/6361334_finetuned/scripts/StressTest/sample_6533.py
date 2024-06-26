passengers_premise = 37300000
passengers_hypothesis = 37300000

# the hypothesis refers to the number of airline passengers traveling to or from the United States in 1979 and 7979
if passengers_hypothesis!= passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers greater than 'passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
