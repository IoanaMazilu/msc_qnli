tab_premise = 80
tip_premise = 1000
tip_hypothesis = 1000

# the hypothesis mentions the amount of the tip, which is also mentioned in the premise
# but the hypothesis does not mention the total amount of the tab
if tip_premise != tip_hypothesis:
    # check if the tip amount in the hypothesis contradicts the tip amount in the premise
    label = "contradiction"
else:
    # if the hypothesis tip amount does not contradict the premise tip amount, but does not mention the tab amount, we can infer neutral
    label = "neutral"

print(label)
