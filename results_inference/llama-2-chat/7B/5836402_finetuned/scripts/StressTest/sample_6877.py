amar_akbar_anthony_ages_premise = 86

# the hypothesis refers to the ages of the same people mentioned in the premise
if amar_akbar_anthony_ages_premise <= hypothesis['total_ages']:
    # check if the estimate of 'total_ages' contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
