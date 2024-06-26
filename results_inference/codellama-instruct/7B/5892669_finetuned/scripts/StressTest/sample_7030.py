start_premise = 7
start_hypothesis = 2

# the hypothesis talks about the starting point of Bill's walk, referenced also in the premise
if start_hypothesis >= start_premise:
    # check if the starting point in the hypothesis contradicts the estimate of less than'start_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the starting point
    # any starting point less than'start_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
