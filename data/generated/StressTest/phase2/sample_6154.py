# Premise: In less than 51 years John will be twice as old as Wilson will be then.
# Hypothesis: In 21 years John will be twice as old as Wilson will be then.
# Golden Label: neutral

years_premise = 51
years_hypothesis = 21

# the hypothesis refers to the time when John will be twice as old as Wilson, also mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the number of years in the hypothesis contradicts the premise estimate of less than 'years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years less than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
