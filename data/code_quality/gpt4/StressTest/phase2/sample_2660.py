years_premise = 15
years_hypothesis = 15

# the hypothesis talks about the same situation as the premise, but with a different time frame
if years_hypothesis >= years_premise:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # the premise gives a fixed time frame
    # any time frame less than 'years_premise' is inconsistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
