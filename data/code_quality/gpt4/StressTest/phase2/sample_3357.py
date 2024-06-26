spots_jack_premise = 2
spots_jack_hypothesis = 5
spots_jill_premise = 7
spots_jill_hypothesis = 7

# the hypothesis refers to the number of spots Jack and Jill collect, which is also mentioned in the premise
if spots_jack_premise > spots_jack_hypothesis:
    # check if the number of spots Jack collects in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
elif spots_jill_premise != spots_jill_hypothesis:
    # check if the number of spots Jill collects in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise ones, but the number of spots Jack collects cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
