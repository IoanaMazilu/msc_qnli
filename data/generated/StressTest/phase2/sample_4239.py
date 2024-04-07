# Premise: His wife Maggie can wash all the windows in 6 hours.
# Hypothesis: His wife Maggie can wash all the windows in more than 5 hours.
# Golden Label: entailment

window_washing_time_premise = 6
window_washing_time_hypothesis = 5

# the hypothesis refers to the time Maggie needs to wash all windows, also mentioned in the premise
if window_washing_time_premise <= window_washing_time_hypothesis:
    # check if the actual 'window_washing_time_premise' contradicts the hypothesis estimate of more than 'window_washing_time_hypothesis'
    label = "neutral"
elif window_washing_time_hypothesis >= window_washing_time_premise:
    # check if the hypothesis estimate contradicts the actual 'window_washing_time_premise'
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the actual 'window_washing_time_premise', we can infer entailment
    label = "entailment"

print(label)

