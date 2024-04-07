# Premise: Ben runs the second leg of the course in less than 63 seconds.
# Hypothesis: Ben runs the second leg of the course in 53 seconds.
# Golden Label: neutral

second_leg_premise = 63
second_leg_hypothesis = 53

# the hypothesis talks about the time Ben takes to run the second leg of the course, referenced also in the premise
if second_leg_hypothesis >= second_leg_premise:
    # check if the hypothesis value contradicts the estimate of less than 'second_leg_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time less than 'second_leg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

