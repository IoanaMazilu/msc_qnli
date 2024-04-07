# Premise: Sandy is younger than Molly by less than 64 years.
# Hypothesis: Sandy is younger than Molly by 14 years.
# Golden Label: neutral

years_difference_premise = 64
years_difference_hypothesis = 14

# the hypothesis refers to the years difference between Sandy and Molly mentioned in the premise
if years_difference_hypothesis >= years_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than 'years_difference_premise'
    label = "contradiction"
elif years_difference_hypothesis <= 0:
    # check if the hypothesis value contradicts the fact that Sandy is younger than Molly
    label = "contradiction"
else:
    # any years difference less than 'years_difference_premise' and greater than 0 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

