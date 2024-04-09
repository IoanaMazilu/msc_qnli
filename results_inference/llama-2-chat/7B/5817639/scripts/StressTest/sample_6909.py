raj_age = 60
roshan_age = 55
ratio = 3

# the hypothesis talks about the age difference and ratio between Roshan and Raj, which are also mentioned in the premise
if roshan_age <= (raj_age - ratio):
    # check if the hypothesis value contradicts the estimate of the age difference between Roshan and Raj
    label = "contradiction"
else:
    # the premise gives an estimate for the age difference and ratio between Roshan and Raj
    # any age difference less than or equal to 6 years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
