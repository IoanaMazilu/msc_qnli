ram_krish_bhim_premise = 30
ram_krish_bhim_hypothesis = 50

# the hypothesis talks about the time it takes for Ram, Krish, and Bhim to complete a work
if ram_krish_bhim_hypothesis <= ram_krish_bhim_premise:
    # check if the hypothesis value contradicts the estimate of less than 30 days
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes to complete a work
    # any time less than 30 days is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
