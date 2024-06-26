passengers_premise = 32300000
passengers_hypothesis = 32300000
year_premise = 1979
year_hypothesis = 1979

# the hypothesis refers to the number of airline passengers traveling to or from the United States
# the premise mentions the number of passengers in 1979
if passengers_hypothesis <= passengers_premise:
    # check if the hypothesis value contradicts the number of passengers in the premise
    label = "contradiction"
elif year_hypothesis < year_premise:
    # check if the hypothesis year is less than the premise year
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers greater than 'passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
