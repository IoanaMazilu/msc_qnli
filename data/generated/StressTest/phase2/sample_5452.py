# Premise: How many miles per hour must Carla drive on average to catch up to him in exactly less than 6 hours if she leaves 30 minutes after Richard?
# Hypothesis: How many miles per hour must Carla drive on average to catch up to him in exactly 3 hours if she leaves 30 minutes after Richard?
# Golden Label: neutral

catchup_time_premise = 6
catchup_time_hypothesis = 3
leave_time_premise = 30
leave_time_hypothesis = 30

# the hypothesis refers to the time Carla needs to catch up to Richard and the time she leaves after Richard, both mentioned in the premise
if catchup_time_hypothesis >= catchup_time_premise:
    # check if the 'catchup_time_hypothesis' contradicts the time estimate in the premise
    label = "contradiction"
elif leave_time_hypothesis != leave_time_premise:
    # check if the 'leave_time_hypothesis' contradicts the leave time reported in the premise
    label = "contradiction"
else:
    # the premise gives only a maximum time for Carla to catch up to Richard
    # any time less than 'catchup_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

