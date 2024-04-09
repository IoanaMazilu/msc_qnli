speed_premise = 40
speed_hypothesis = 10

# the hypothesis refers to the speed at which Bob drives
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif speed_premise!= speed_hypothesis:
    # check if the hypothesis value contradicts the estimate of the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis value and the premise estimate do not contradict, we can infer neutrality
    label = "neutral"

print(label)
