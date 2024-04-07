# Premise: Tom goes after more than 4 P.
# Hypothesis: Tom goes after 8 P.
# Golden Label: neutral

time_premise = 4
time_hypothesis = 8

# the hypothesis talks about the time when Tom goes, referenced also in the premise
if time_hypothesis <= time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time greater than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

