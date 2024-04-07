# Premise: After less than 8 years, Sandy’s age will be 42 years.
# Hypothesis: After 6 years, Sandy’s age will be 42 years.
# Golden Label: neutral

years_until_42_premise = 8
years_until_42_hypothesis = 6

# the hypothesis refers to the number of years until Sandy's age will be 42, which is also mentioned in the premise
if years_until_42_hypothesis >= years_until_42_premise:
    # check if the hypothesis value contradicts the estimate of less than 'years_until_42_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years until Sandy will be 42
    # any number of years less than 'years_until_42_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

