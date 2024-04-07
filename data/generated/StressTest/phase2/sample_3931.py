# Premise: less than 70 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Hypothesis: 60 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Golden Label: neutral

carpet_coverage_premise = 70
carpet_coverage_hypothesis = 60

# the hypothesis refers to the percentage of the floor covered by the carpet, also mentioned in the premise
if carpet_coverage_hypothesis >= carpet_coverage_premise:
    # check if the carpet coverage percentage in the hypothesis contradicts the premise's estimate of less than 'carpet_coverage_premise'
    label = "contradiction"
elif carpet_coverage_hypothesis < carpet_coverage_premise:
    # any percentage less than 'carpet_coverage_premise' is consistent with the premise, thus can be inferred as entailed from the premise
    label = "entailment"

print(label)

