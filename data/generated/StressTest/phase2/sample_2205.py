# Premise: If exactly 4 of the packages Steve bought contained 7 pens, how many pens did Steve buy?
# Hypothesis: If exactly less than 7 of the packages Steve bought contained 7 pens, how many pens did Steve buy?
# Golden Label: entailment

packages_premise = 4
pens_per_package_premise = 7
packages_hypothesis = 7
pens_per_package_hypothesis = 7

# the hypothesis refers to the number of packages Steve bought and the number of pens contained in each package
if packages_hypothesis >= packages_premise:
    # check if the number of packages in the hypothesis contradicts the number of packages mentioned in the premise
    label = "contradiction"
elif pens_per_package_hypothesis != pens_per_package_premise:
    # check if the number of pens per package in the hypothesis contradicts the number of pens per package reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

