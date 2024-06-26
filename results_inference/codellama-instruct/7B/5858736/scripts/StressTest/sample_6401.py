passengers_miami_premise = 1/2
passengers_kennedy_premise = 1/2
passengers_logan_premise = 4

passengers_miami_hypothesis = 3/2
passengers_kennedy_hypothesis = 3/2
passengers_logan_hypothesis = 4

# the hypothesis refers to the number of passengers that used Logan Airport, referenced also in the premise
if passengers_logan_hypothesis <= passengers_logan_premise:
    # check if the hypothesis value contradicts the estimate of more than 'passengers_logan_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers that used Logan Airport
    # any number of passengers greater than 'passengers_logan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
