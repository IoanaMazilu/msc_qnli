# Premise: If exactly 4 of the packages Steve bought contained 7 pens, how many pens did Steve buy?
# Hypothesis: If exactly more than 4 of the packages Steve bought contained 7 pens, how many pens did Steve buy?
# Golden Label: contradiction

packages_premise = 4
packages_hypothesis = 4
pens_per_package = 7

# the hypothesis refers to the number of packages that Steve bought and the number of pens per package, both mentioned in the premise
if packages_hypothesis > packages_premise:
    # check if the number of packages in the hypothesis contradicts the exact number of packages in the premise
    label = "contradiction"
elif packages_hypothesis == packages_premise:
    # if the number of packages in the hypothesis is the same as the exact number in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of packages in the hypothesis is less than the exact number in the premise, it does not contradict the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

