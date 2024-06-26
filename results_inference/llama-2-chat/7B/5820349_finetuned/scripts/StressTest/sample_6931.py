years_premise = 2
years_hypothesis = 6
age_premise = 30
age_hypothesis = 30

# the hypothesis talks about Sandy's age after a number of years, referenced also in the premise
if age_hypothesis!= age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif years_hypothesis <= years_premise:
    # check if the hypothesis number of years contradicts the premise number of years
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
