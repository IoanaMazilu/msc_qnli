t_shirts_premise = 8
t_shirts_hypothesis = 8

# the hypothesis talks about the number of t-shirts bought and the average price, which is also referred to in the premise
if t_shirts_hypothesis <= t_shirts_premise:
    # check if the hypothesis value contradicts the estimate of 't_shirts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of t-shirts and the average price
    # any number of t-shirts and average price consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
