words_premise = 8
words_hypothesis = 8
rate_premise = 4
rate_hypothesis = 4

# the hypothesis refers to the number of words James can type in a certain amount of minutes
if words_hypothesis >= words_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
