download_speed_percentage_premise = 0.8
download_speed_percentage_hypothesis = 0.8

# the hypothesis mentions the percentage of broadband lines in EU with download speeds of two mbs or greater, which is also referenced in the premise
if download_speed_percentage_hypothesis!= download_speed_percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
