t_shirts_premise = 4
t_shirts_hypothesis = 5

# the hypothesis talks about the number of t-shirts returned by Sanoop, and the premise gives an estimate of the number of t-shirts returned
if t_shirts_hypothesis <= t_shirts_premise:
    # check if the hypothesis value contradicts the estimate of more than 't_shirts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of t-shirts returned, and any number of t-shirts greater than 't_shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
