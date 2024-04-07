# Premise: City A to city B, Michael drove for 1 hour at 80 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Michael drove for less than 1 hour at 80 mph and for 3 hours at 60 mph.
# Golden Label: contradiction

drive_hour_80mph_premise = 1
drive_hour_80mph_hypothesis = 1
drive_hour_60mph_premise = 3
drive_hour_60mph_hypothesis = 3

# the hypothesis refers to the driving times at different speeds mentioned in the premise
if drive_hour_80mph_hypothesis >= drive_hour_80mph_premise:
    # check if the hypothesis value contradicts the premise's driving time at 80 mph
    label = "contradiction"
elif drive_hour_60mph_hypothesis != drive_hour_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

