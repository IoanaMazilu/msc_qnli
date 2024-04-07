# Premise: After 6 years, Sandy’s age will be 30 years.
# Hypothesis: After more than 2 years, Sandy’s age will be 30 years.
# Golden Label: entailment

years_premise = 6
years_hypothesis = 2
age_premise = 30
age_hypothesis = 30

# the hypothesis refers to the age of Sandy after a certain number of years, also mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif age_hypothesis != age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of years and age
    # the hypothesis claims a number of years less than the one in the premise and the same age, which cannot be true
    label = "neutral"

print(label)

