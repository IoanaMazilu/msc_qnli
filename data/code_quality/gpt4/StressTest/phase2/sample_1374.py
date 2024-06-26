years_hence_premise = 15
years_hence_hypothesis = 45

# the hypothesis talks about the number of years hence, which is also referenced in the premise
if years_hence_hypothesis <= years_hence_premise:
    # check if the hypothesis value contradicts the premise value of 'years_hence_premise'
    label = "contradiction"
elif years_hence_hypothesis > years_hence_premise:
    # the premise gives a specific number for the years hence
    # any number of years hence less than 'years_hence_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
