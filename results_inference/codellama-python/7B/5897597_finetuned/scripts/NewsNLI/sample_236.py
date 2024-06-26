broadband_lines_premise = 0.8
broadband_lines_hypothesis = 0.8

# the hypothesis mentions the percentage of broadband lines in the EU with download speeds of two mbs or greater, which is also mentioned in the premise
if broadband_lines_hypothesis!= broadband_lines_premise:
    # check if the percentage of broadband lines in the EU with download speeds of two mbs or greater in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
