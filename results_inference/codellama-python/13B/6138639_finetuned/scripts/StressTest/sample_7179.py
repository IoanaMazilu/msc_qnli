time_42mph_premise = 1
time_42mph_hypothesis = 5
time_60mph_premise = 3
time_60mph_hypothesis = 3

# the hypothesis refers to the time Andrew spent driving at 42 mph and 60 mph, which is also mentioned in the premise
if time_42mph_hypothesis <= time_42mph_premise:
    # check if the hypothesis value contradicts the time Andrew spent driving at 42 mph in the premise
    label = "contradiction"
elif time_60mph_hypothesis!= time_60mph_premise:
    # check if the time Andrew spent driving at 60 mph in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives the exact time Andrew spent driving at 42 mph and 60 mph
    # any time less than 'time_42mph_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
