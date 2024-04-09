t_shirts_premise = 8
t_shirts_hypothesis = 3

# the hypothesis talks about the number of t-shirts bought and their average price
if t_shirts_hypothesis <= t_shirts_premise:
    # check if the hypothesis value contradicts the estimate of 't_shirts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of t-shirts bought
    # any number of t-shirts greater than 't_shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
