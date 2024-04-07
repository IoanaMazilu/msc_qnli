# Premise: Ben runs the second leg of the course in 53 seconds.
# Hypothesis: Ben runs the second leg of the course in less than 63 seconds.
# Golden Label: entailment

second_leg_time_premise = 53
second_leg_time_hypothesis = 63

# the hypothesis refers to the time Ben took to run the second leg of the course, which is also mentioned in the premise
if second_leg_time_premise >= second_leg_time_hypothesis:
    # check if the time 'second_leg_time_premise' contradicts the estimation of less than 'second_leg_time_hypothesis' seconds
    label = "contradiction"
else:
    # if the time Ben took in the premise is less than the 'second_leg_time_hypothesis', it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)

