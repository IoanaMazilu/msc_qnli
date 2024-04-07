# Premise: less than 45 years hence, Rohan will be just four times as old as he was 15 years ago.
# Hypothesis: 15 years hence, Rohan will be just four times as old as he was 15 years ago.
# Golden Label: neutral

years_hence_premise = 45
years_hence_hypothesis = 15

# the hypothesis talks about a certain condition regarding Rohan's age, referenced also in the premise
if years_hence_hypothesis >= years_hence_premise:
    # check if the hypothesis value contradicts the estimate of less than 'years_hence_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years less than 'years_hence_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

