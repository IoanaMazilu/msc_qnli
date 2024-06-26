scott_avg_premise = 58
scott_avg_hypothesis = 78

# the hypothesis refers to the average golf score in the premise
if scott_avg_premise <= scott_avg_hypothesis:
    # check if the estimate of'scott_avg_hypothesis' contradicts the premise
    label = "contradiction"
elif scott_avg_hypothesis!= scott_avg_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value and premise are consistent, we can infer neutrality
    label = "neutral"

print(label)
