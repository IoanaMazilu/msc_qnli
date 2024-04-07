# Premise: Carl can wash all the windows of his house in 6 hours.
# Hypothesis: Carl can wash all the windows of his house in more than 1 hours.
# Golden Label: entailment

windows_washing_time_premise = 6
windows_washing_time_hypothesis = 1

# the hypothesis talks about the time Carl takes to wash all the windows of his house, which is also referred to in the premise
if windows_washing_time_premise <= windows_washing_time_hypothesis:
    # check if the actual time Carl takes to wash all windows mentioned in the premise contradicts the estimate of more than 'windows_washing_time_hypothesis' hours
    label = "contradiction"
else:
    # if the premise does not contradict the hypothesis' estimate about Carl's time to wash all windows, we can infer entailment
    label = "entailment"

print(label)

