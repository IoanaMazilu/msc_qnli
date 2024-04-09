age_premise = 1/6
age_hypothesis = 1/6

# the hypothesis talks about Ayisha's age being less than 1/6 of her father's age
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Ayisha's age
    # any age less than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
