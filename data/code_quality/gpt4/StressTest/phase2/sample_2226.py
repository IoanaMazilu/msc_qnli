miami_kennedy_ratio_premise = 1/2
miami_kennedy_ratio_hypothesis = 7/2
miami_logan_ratio_premise = 4
miami_logan_ratio_hypothesis = 4

# the hypothesis refers to the ratios of passengers that used Miami, Kennedy and Logan airport mentioned in the premise
# first compare the miami to kennedy ratios
if miami_kennedy_ratio_premise < miami_kennedy_ratio_hypothesis:
    # check if the 'miami_kennedy_ratio_hypothesis' contradicts the ratio mentioned in the premise
    label = "contradiction"
# then compare the miami to logan ratios
elif miami_logan_ratio_premise != miami_logan_ratio_hypothesis:
    # check if the 'miami_logan_ratio_hypothesis' contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
