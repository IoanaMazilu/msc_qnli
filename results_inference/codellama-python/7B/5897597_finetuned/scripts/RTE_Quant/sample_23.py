peak_height_premise = 8586
peak_height_hypothesis = 8586

# the hypothesis talks about the height of the peak, which is also mentioned in the premise
if peak_height_hypothesis!= peak_height_premise:
    # check if the height of the peak in the hypothesis contradicts the height of the peak in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
