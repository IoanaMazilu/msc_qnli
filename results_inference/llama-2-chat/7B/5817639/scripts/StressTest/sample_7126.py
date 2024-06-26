total_time_premise = float(input("Premise: How many miles from home can Aaron jog so that he spends a total of more than 1 hours jogging and walking? "))
total_time_hypothesis = float(input("Hypothesis: How many miles from home can Aaron jog so that he spends a total of 3 hours jogging and walking? "))

# the hypothesis talks about the total time spent jogging and walking, referenced also in the premise
if total_time_hypothesis <= total_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'total_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total time spent jogging and walking
    # any total time greater than 'total_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
