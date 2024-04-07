# Premise: City A to city B, Andrew drove for 1 hr at 46 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for less than 7 hr at 46 mph and for 3 hours at 60 mph.
# Golden Label: entailment

driving_time_46mph_premise = 1
driving_time_46mph_hypothesis = 7
driving_time_60mph_premise = 3
driving_time_60mph_hypothesis = 3

# the hypothesis refers to the driving time at 46 mph and 60 mph mentioned in the premise
if driving_time_46mph_hypothesis <= driving_time_46mph_premise:
    # check if the estimate of 'driving_time_46mph_hypothesis' contradicts the driving time at 46 mph in the premise
    label = "contradiction"
elif driving_time_60mph_hypothesis != driving_time_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

