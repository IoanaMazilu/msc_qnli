father_age_premise = 2*shankar_age_premise = 80

# the hypothesis refers to the number of years until Ayisha's father's age will be twice Shankar's age
if father_age_premise >= 80:
    # check if the estimate of 'father_age_premise' contradicts the number of years until Ayisha's father's age will be twice Shankar's age in the hypothesis
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years until Ayisha's father's age will be twice Shankar's age
    # any number of years less than 'father_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
