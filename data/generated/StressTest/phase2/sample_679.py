# Premise: City A to city B, Raja drove for less than 4 hour at 72 mph and for 3 hours at 80 mph.
# Hypothesis: City A to city B, Raja drove for 1 hour at 72 mph and for 3 hours at 80 mph.
# Golden Label: neutral

time_driven_72mph_premise = 4
time_driven_72mph_hypothesis = 1
time_driven_80mph_premise = 3
time_driven_80mph_hypothesis = 3

# the hypothesis refers to the duration Raja drove at 72 mph and 80 mph mentioned in the premise
if time_driven_72mph_hypothesis >= time_driven_72mph_premise:
    # check if the duration at 72 mph in the hypothesis contradicts the estimate of less than 'time_driven_72mph_premise' in the premise
    label = "contradiction"
elif time_driven_80mph_hypothesis != time_driven_80mph_premise:
    # check if the duration at 80 mph in the hypothesis contradicts the exact duration at 80 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

