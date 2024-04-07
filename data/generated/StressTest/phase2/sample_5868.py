# Premise: Ed drives at a constant speed of 31 km per hour.
# Hypothesis: Ed drives at a constant speed of less than 51 km per hour.
# Golden Label: entailment

speed_premise = 31
speed_hypothesis = 51

# the hypothesis talks about the speed at which Ed drives, which is also mentioned in the premise
if speed_premise >= speed_hypothesis:
    # check if the speed in the premise contradicts the 'less than speed_hypothesis' estimate
    label = "contradiction"
else:
    # the premise explicitly mentions the speed of 'speed_premise'
    # so any speed less than 'speed_hypothesis' would not contradict the premise, but the exact speed cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

