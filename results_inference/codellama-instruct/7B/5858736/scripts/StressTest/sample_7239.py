age_ayisha_premise = 1/6
age_ayisha_hypothesis = 3/6

# the hypothesis talks about the age of Ayisha, referenced also in the premise
if age_ayisha_hypothesis <= age_ayisha_premise:
    # check if the hypothesis value contradicts the estimate of less than 'age_ayisha_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Ayisha's age
    # any number of years less than 'age_ayisha_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
