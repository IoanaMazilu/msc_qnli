john_age_subtract_premise = 6
john_age_subtract_hypothesis = 4
age_ratio = 18

# the hypothesis refers to the same procedure to estimate Anup's age mentioned in the premise
if john_age_subtract_hypothesis >= john_age_subtract_premise:
    # check if the hypothesis value contradicts the estimate of 'john_age_subtract_premise'
    label = "contradiction"
else:
    # the premise gives only a specific value for the number of years to subtract
    # any number less than 'john_age_subtract_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
