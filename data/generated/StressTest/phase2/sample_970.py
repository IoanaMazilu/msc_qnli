# Premise: Jake can dig a well in less than 66 days.
# Hypothesis: Jake can dig a well in 16 days.
# Golden Label: neutral

dig_time_premise = 66
dig_time_hypothesis = 16

# the hypothesis talks about the time Jake takes to dig a well, referenced also in the premise
if dig_time_hypothesis >= dig_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'dig_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time less than 'dig_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

