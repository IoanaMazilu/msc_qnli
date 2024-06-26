average_runs_premise = float(input("Premise: "))
average_runs_hypothesis = float(input("Hypothesis: "))

# the hypothesis talks about the number of runs in a certain context, referenced also in the premise
if average_runs_hypothesis <= average_runs_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_runs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of runs
    # any number of runs greater than 'average_runs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
