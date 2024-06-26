download_speed_premise = 2
download_speed_hypothesis = 2
percentage_broadband_lines_premise = 0.8
percentage_broadband_lines_hypothesis = 0.8

# the hypothesis mentions the percentage of broadband lines and the download speed, which are also mentioned in the premise
if download_speed_hypothesis!= download_speed_premise:
    # check if the download speed in the hypothesis contradicts the download speed reported in the premise
    label = "contradiction"
elif percentage_broadband_lines_hypothesis!= percentage_broadband_lines_premise:
    # check if the percentage of broadband lines from the hypothesis contradicts the percentage of broadband lines in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
