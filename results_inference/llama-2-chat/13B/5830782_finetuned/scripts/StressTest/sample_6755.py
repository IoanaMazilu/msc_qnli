time_premise = 8
time_hypothesis = 8

# the hypothesis refers to the time when Ana goes, which is also mentioned in the premise
if time_hypothesis >= time_premise:
    # check if the hypothesis value contradicts the premise that Ana goes before 'time_premise'
    label = "contradiction"
else:
    # the premise gives a specific time when Ana goes
    # any time less than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
