# defining the variables
sheep_horses_ratio_premise = 1/7
sheep_horses_ratio_hypothesis = 6/7
sheep_horses_ratio_premise_hypothesis = 1/7

# the hypothesis talks about the sheep and horses ratio at the Stewart farm
if sheep_horses_ratio_premise <= sheep_horses_ratio_hypothesis:
    # check if the hypothesis value contradicts the premise ratio
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
