# Premise: His wife Maggie can wash all the windows in more than 5 hours.
# Hypothesis: His wife Maggie can wash all the windows in 6 hours.
# Golden Label: neutral

windows_washing_time_premise = 5
windows_washing_time_hypothesis = 6

# the hypothesis talks about the time Maggie needs to wash all the windows, referenced also in the premise
if windows_washing_time_hypothesis <= windows_washing_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'windows_washing_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the washing time
    # any washing time greater than 'windows_washing_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

