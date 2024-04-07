# Premise: Carl can wash all the windows of his house in 6 hours.
# Hypothesis: Carl can wash all the windows of his house in less than 6 hours.
# Golden Label: contradiction

windows_washing_time_premise = 6
windows_washing_time_hypothesis = 6

# the hypothesis talks about the time Carl takes to wash all windows, referenced also in the premise
if windows_washing_time_hypothesis < windows_washing_time_premise:
    # check if the hypothesis value contradicts the exact time of 'windows_washing_time_premise'
    label = "contradiction"
elif windows_washing_time_hypothesis > windows_washing_time_premise:
    # check if the hypothesis value contradicts the exact time of 'windows_washing_time_premise'
    label = "contradiction"
else:
    # if the hypothesis value is equal to the premise one, we can infer entailment
    label = "entailment"

print(label)

