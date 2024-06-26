miami_kennedy_ratio_premise = 8/2
miami_kennedy_ratio_hypothesis = 1/2

# the hypothesis talks about the ratio of passengers that used Miami Airport to those that used Kennedy Airport
# this ratio is also referenced in the premise
if miami_kennedy_ratio_hypothesis!= miami_kennedy_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise and hypothesis ratios are the same
    label = "entailment"

print(label)
