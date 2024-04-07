# Premise: Steve bought a total of more than 3 packages of pens, and each package contained either 3 or 7 pens.
# Hypothesis: Steve bought a total of 6 packages of pens, and each package contained either 3 or 7 pens.
# Golden Label: neutral

packages_bought_premise = 3
packages_bought_hypothesis = 6

# the hypothesis refers to the number of packages bought mentioned in the premise
if packages_bought_hypothesis <= packages_bought_premise:
    # check if the number of packages bought in the hypothesis contradicts the estimate of more than 'packages_bought_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of packages bought
    # any number of packages greater than 'packages_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

