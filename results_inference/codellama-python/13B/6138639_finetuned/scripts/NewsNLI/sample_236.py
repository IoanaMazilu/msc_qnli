broadband_speed_premise = 80
broadband_speed_hypothesis = 80

# the hypothesis mentions the percentage of broadband lines in the EU with download speeds of two mbs or greater, which is also referenced in the premise
if broadband_speed_hypothesis!= broadband_speed_premise:
    # check if the percentage of broadband lines in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
