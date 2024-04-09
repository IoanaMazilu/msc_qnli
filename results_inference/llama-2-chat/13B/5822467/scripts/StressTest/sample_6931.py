age_premise = 30
age_hypothesis = 30
years_premise = 2
years_hypothesis = 6

# the hypothesis talks about Sandy's age after 6 years, referenced also in the premise
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of 'age_premise'
    label = "contradiction"
elif years_hypothesis <= years_premise:
    # check if the estimate of 'years_hypothesis' contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Sandy's age after 2 years
    # any age after 2 years consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
