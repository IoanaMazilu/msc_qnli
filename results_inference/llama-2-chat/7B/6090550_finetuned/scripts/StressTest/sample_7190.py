suggested_time_premise = 12
suggested_time_hypothesis = 62

# the hypothesis refers to the time at which the train leaves Jammu for Chennai, which is also mentioned in the premise
if suggested_time_hypothesis == suggested_time_premise:
    # check if the time in the hypothesis matches the time mentioned in the premise
    label = "entailment"
else:
    # if the time in the hypothesis does not match the time mentioned in the premise, we have a contradiction
    label = "contradiction"

print(label)
