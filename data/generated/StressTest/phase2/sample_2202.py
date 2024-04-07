# Premise: Steve bought a total of 6 packages of pens, and each package contained either 3 or 7 pens.
# Hypothesis: Steve bought a total of more than 3 packages of pens, and each package contained either 3 or 7 pens.
# Golden Label: entailment

total_packages_premise = 6
total_packages_hypothesis = 3

# the hypothesis refers to the number of packages of pens bought by Steve, which is also mentioned in the premise
if total_packages_premise <= total_packages_hypothesis:
    # check if the estimate in 'total_packages_hypothesis' contradicts the number of packages in the premise
    label = "contradiction"
else:
    # if the number of packages in the hypothesis is less than or equal to the number of packages in the premise, we can infer entailment
    label = "entailment"

print(label)
