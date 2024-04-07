# Premise: After more than 2 years, Sandy’s age will be 30 years.
# Hypothesis: After 6 years, Sandy’s age will be 30 years.
# Golden Label: neutral

years_premise = 2
age_premise = 30
years_hypothesis = 6
age_hypothesis = 30

# the hypothesis talks about Sandy's age after a certain number of years, which is also referenced in the premise
if (age_hypothesis != age_premise) or (years_hypothesis <= years_premise):
    # check if the hypothesized age contradicts the age mentioned in the premise, or if the hypothesized number of years contradicts the premise
    label = "contradiction"
else:
    # the premise gives only a lower bound for the number of years
    # any number of years greater than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

