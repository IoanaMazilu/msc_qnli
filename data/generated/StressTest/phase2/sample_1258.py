# Premise: Altogether, Steve is spending less than 7 hours a day on the roads.
# Hypothesis: Altogether, Steve is spending 6 hours a day on the roads.
# Golden Label: neutral

time_spent_premise = 7
time_spent_hypothesis = 6

# the hypothesis talks about the time Steve spends on the roads, referenced also in the premise
if time_spent_hypothesis >= time_spent_premise:
    # check if the hypothesis value contradicts the estimate of less than 'time_spent_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time spent on roads
    # any amount of time less than 'time_spent_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

