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
