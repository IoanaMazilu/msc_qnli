years_premise = 2
years_hypothesis = 6
interest_rate = 4

# the hypothesis talks about the number of years and interest rate, referenced also in the premise
if years_hypothesis!= years_premise:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years equal to 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
