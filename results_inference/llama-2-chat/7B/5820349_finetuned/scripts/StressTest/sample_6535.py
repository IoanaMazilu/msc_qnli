miami_kennedy_ratio_premise = 7/3
miami_kennedy_ratio_hypothesis = 1/3

# the hypothesis talks about the ratio of passengers that used Miami Airport to those that used Kennedy Airport, which is also referenced in the premise
if miami_kennedy_ratio_hypothesis!= miami_kennedy_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # the premise gives a specific ratio for the passengers that used Miami Airport to those that used Kennedy Airport
    # any ratio equal to'miami_kennedy_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
