# Premise: It added that 80 per cent of broadband lines in the EU had download speeds of two mbs or greater.
# Hypothesis: European Union:80 per cent of broadband lines in EU have download speeds of two mbs-plus.
# Golden Label: entailment

percentage_premise = 80
percentage_hypothesis = 80
download_speed_premise = 2
download_speed_hypothesis = 2

# the hypothesis mentions the percentage of broadband lines and the download speed in EU, which are also mentioned in the premise
if percentage_hypothesis != percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
elif download_speed_hypothesis != download_speed_premise:
    # check if the download speed from the hypothesis contradicts the download speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

