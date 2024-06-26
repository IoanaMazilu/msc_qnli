raise_avg_premise = 6
raise_avg_hypothesis = 2

# the hypothesis talks about raising the average score, referred also in the premise
if raise_avg_hypothesis >= raise_avg_premise:
    # check if the hypothesis value contradicts the estimate of less than 'raise_avg_premise'
    label = "contradiction"
elif raise_avg_hypothesis < raise_avg_premise:
    # the premise gives an estimate for the raise in average score
    # any raise less than 'raise_avg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
