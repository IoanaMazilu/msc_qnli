# define variables with representative names for the numerical entities in both inputs
molly_age_premise = 18
molly_age_hypothesis = 18 + 6

# extract all quantities as valid numbers (integers or floats)
molly_age_premise_int = int(molly_age_premise)
molly_age_hypothesis_int = int(molly_age_hypothesis)

# use brief comments to explain what comparison we do between the defined variables
# the hypothesis talks about Molly's age in more than 18 years
if molly_age_hypothesis_int > molly_age_premise_int:
    # check if the hypothesis value contradicts the estimate of'molly_age_premise'
    label = "contradiction"
elif molly_age_hypothesis_int == molly_age_premise_int:
    # the premise gives only an estimate for Molly's age
    # any number of years greater than or equal to'molly_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis value is consistent with the estimate of'molly_age_premise'
    # we can infer entailment
    label = "entailment"

print(label)
