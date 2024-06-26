premise_age = 54
hypothesis_age = 34
baby_sitting_years = 10

# the hypothesis refers to the age of Jane and the number of years she stopped baby-sitting
if hypothesis_age < premise_age:
    # check if the hypothesis value contradicts the estimate of less than 'premise_age'
    label = "contradiction"
elif baby_sitting_years!= 10:
    # check if the number of years she stopped baby-sitting in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Jane and the number of years she stopped baby-sitting
    # any age and number of years greater than the premise values are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
