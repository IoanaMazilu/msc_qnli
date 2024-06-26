percentage_boys_premise = 0.3
percentage_boys_hypothesis = 0.1

# the hypothesis refers to the percentage of boys in the school population mentioned in the premise
if percentage_boys_premise <= percentage_boys_hypothesis:
    # check if the estimate of 'percentage_boys_hypothesis' contradicts the percentage of boys in the premise
    label = "contradiction"
elif percentage_boys_hypothesis < percentage_boys_premise:
    # check if the percentage of boys in the hypothesis is less than the percentage of boys in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
