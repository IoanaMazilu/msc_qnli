# Premise: If exactly less than 7 of the packages Steve bought contained 7 pens, how many pens did Steve buy?
# Hypothesis: If exactly 4 of the packages Steve bought contained 7 pens, how many pens did Steve buy?
# Golden Label: neutral

packages_premise = 7
packages_hypothesis = 4
pens_per_package = 7

# the hypothesis refers to the number of packages Steve bought mentioned in the premise
if packages_premise <= packages_hypothesis:
    # check if the number of 'packages_hypothesis' contradicts the number of packages in the premise
    label = "contradiction"
elif packages_premise > packages_hypothesis:
    # check if the number of 'packages_hypothesis' is less than the number of packages in the premise
    # it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

