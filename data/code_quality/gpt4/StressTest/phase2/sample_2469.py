driving_duration_50mph_premise = 1
driving_duration_50mph_hypothesis = 4
driving_duration_60mph_premise = 3
driving_duration_60mph_hypothesis = 3

# the hypothesis talks about the driving duration at 50mph and 60mph between city A and city B
if driving_duration_50mph_hypothesis <= driving_duration_50mph_premise:
    # check if the hypothesis value contradicts the duration of driving at 50mph in the premise
    label = "contradiction"
elif driving_duration_60mph_hypothesis != driving_duration_60mph_premise:
    # check if the driving duration at 60mph in the hypothesis contradicts the driving duration at 60mph reported in the premise
    label = "contradiction"
else:
    # the premise gives exact values for the driving duration at 50mph and 60mph
    # the hypothesis states less than 4 hours at 50mph, which is more than the premise value, and therefore cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
