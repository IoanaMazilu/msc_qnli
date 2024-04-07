# Premise: less than 85 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Hypothesis: 75 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Golden Label: neutral

carpet_coverage_premise = 85
carpet_coverage_hypothesis = 75
carpet_size = 4 * 9 # carpet size in square feet

# the hypothesis refers to the percentage of Andrea's living room floor covered by the carpet mentioned in the premise
if carpet_coverage_hypothesis >= carpet_coverage_premise:
    # check if the hypothesis value contradicts the estimate of less than 'carpet_coverage_premise'
    label = "contradiction"
elif carpet_coverage_premise < carpet_coverage_hypothesis:
    # check if the 'carpet_coverage_premise' contradicts the estimate of the hypothesis
    label = "contradiction"
else:
    # any percentage less than 'carpet_coverage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

