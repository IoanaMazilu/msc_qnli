# Premise: If there are less than 8 boxes of cigarettes in one case, how many cases can Kramer pack in 2 hours?
# Hypothesis: If there are 5 boxes of cigarettes in one case, how many cases can Kramer pack in 2 hours?
# Golden Label: neutral

cigarettes_box_premise = 8
cigarettes_box_hypothesis = 5

# the hypothesis refers to the number of boxes of cigarettes in one case mentioned in the premise
if cigarettes_box_hypothesis >= cigarettes_box_premise:
    # check if the number of 'cigarettes_box_hypothesis' contradicts the estimate of less than 'cigarettes_box_premise'
    label = "contradiction"
else:
    # If the number of 'cigarettes_box_hypothesis' is less than 'cigarettes_box_premise', it does not contradict the premise
    # but it cannot be explicitly entailed from the premise since the premise does not provide an exact number
    label = "neutral"

print(label)

