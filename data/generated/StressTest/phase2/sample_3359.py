# Premise: Jack only collects the ones with 2 spots, and Jill only collects the ones with 7 spots.
# Hypothesis: Jack only collects the ones with 1 spots, and Jill only collects the ones with 7 spots.
# Golden Label: contradiction

spots_jack_premise = 2
spots_jack_hypothesis = 1
spots_jill_premise = 7
spots_jill_hypothesis = 7

# the hypothesis refers to the number of spots Jack and Jill collect, mentioned in the premise
if spots_jack_premise != spots_jack_hypothesis:
    # check if the number of spots Jack collects in the hypothesis contradicts the number of spots Jack collects in the premise
    label = "contradiction"
elif spots_jill_hypothesis != spots_jill_premise:
    # check if the number of spots Jill collects in the hypothesis contradicts the number of spots Jill collects in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise values, therefore it's neutral
    label = "neutral"

print(label)

