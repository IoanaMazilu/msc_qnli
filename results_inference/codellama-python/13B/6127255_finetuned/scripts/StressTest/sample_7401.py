#drive_time_46mph_premise = 1
#drive_time_46mph_hypothesis = 7
#drive_time_60mph_premise = 3
#drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving times at different speeds mentioned in the premise
# first, we check the driving time at 46 mph
if drive_time_46mph_hypothesis < drive_time_46mph_premise:
    # check if the hypothesis value contradicts the driving time at 46 mph in the premise
    label = "contradiction"
elif drive_time_60mph_hypothesis!= drive_time_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
#