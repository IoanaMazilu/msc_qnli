time_premise = 7
time_hypothesis = 6

# the hypothesis presents a more precise time than the premise
if time_hypothesis >= time_premise:
    # check if the time in the hypothesis contradicts the premise's estimate of less than 'time_premise' years
    label = "contradiction"
elif time_hypothesis < time_premise:
    # any time less than 'time_premise' years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
