# define variables with representative names for the numerical entities in both inputs
age_sandy_premise = 4
age_sandy_hypothesis = 6

# extract all quantities as valid numbers (integers or floats)
age_sandy_premise = int(age_sandy_premise)
age_sandy_hypothesis = int(age_sandy_hypothesis)

# use brief comments to explain what comparison you do between the defined variables
if age_sandy_hypothesis <= age_sandy_premise:
    # check if the hypothesis value contradicts the estimate of more than 'age_sandy_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Sandy's age
    # any number of years greater than 'age_sandy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
