years_premise = 2
years_hypothesis = 2
interest_rate = 4

# the hypothesis talks about the number of years and the interest rate, both mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the hypothesis value contradicts the premise of less than 'years_premise' years
    label = "contradiction"
else:
    # the premise gives a maximum number of years
    # any number of years less than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
