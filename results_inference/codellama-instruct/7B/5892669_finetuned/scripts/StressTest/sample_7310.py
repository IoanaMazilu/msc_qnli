words_premise = 8
words_hypothesis = 8
rate_premise = 4
rate_hypothesis = 4

# the hypothesis refers to the number of words James types and the typing rate, both mentioned in the premise
if words_hypothesis >= words_premise:
    # check if the hypothesis value contradicts the premise of less than 'words_premise'
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the typing rate in the hypothesis contradicts the typing rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
