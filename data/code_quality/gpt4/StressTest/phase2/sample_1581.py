#time spent driving at 80mph
drive_time_80mph_premise = 1
drive_time_80mph_hypothesis = 4

#time spent driving at 60mph
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the time Michael spent driving at 80mph and 60mph from city A to city B

if drive_time_80mph_premise > drive_time_80mph_hypothesis:
    # check if the time spent driving at 80mph in the premise contradicts the estimate of less than 'drive_time_80mph_hypothesis'
    label = "contradiction"
elif drive_time_60mph_premise != drive_time_60mph_hypothesis:
    # check if the time spent driving at 60mph in the hypothesis contradicts the time spent driving at 60mph in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
