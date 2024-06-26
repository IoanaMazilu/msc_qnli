cookies_eaten_premise = 7/8
cookies_eaten_hypothesis = 1/8

# the hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler mentioned in the premise
if cookies_eaten_hypothesis >= cookies_eaten_premise:
    # check if the estimate of 'cookies_eaten_hypothesis' contradicts the number of cookies eaten by Michael in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
