jack_walked_premise = 4
jack_walked_hypothesis = 3

# the hypothesis refers to the distance walked and the time taken, which are also present in the premise
if jack_walked_hypothesis <= jack_walked_premise:
    # check if the estimate of 'jack_walked_hypothesis' contradicts the distance walked in the premise
    label = "contradiction"
elif jack_walked_hypothesis > jack_walked_premise:
    # check if the hypothesis value contradicts the estimate of 'jack_walked_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
