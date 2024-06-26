borrowed_pounds_premise = 6500
borrowed_pounds_hypothesis = 3500

# the hypothesis refers to the amount borrowed by Dana for her college education mentioned in the premise
if borrowed_pounds_premise <= borrowed_pounds_hypothesis:
    # check if the estimate of 'borrowed_pounds_hypothesis' contradicts the amount borrowed in the premise
    label = "contradiction"
elif borrowed_pounds_hypothesis > borrowed_pounds_premise:
    # check if the amount borrowed in the hypothesis is greater than the amount borrowed in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
