years_subtracted_premise = 6
years_subtracted_hypothesis = 7

# the hypothesis refers to the number of years subtracted from Arun's age, as obtained from the premise
if years_subtracted_hypothesis <= years_subtracted_premise:
    # check if the number of years subtracted in the hypothesis contradicts the number of years subtracted in the premise
    label = "contradiction"
else:
    # the premise only details a very specific calculation
    # any number of years subtracted that is more than 'years_subtracted_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
