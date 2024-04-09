work_time_premise = 11
work_time_hypothesis = 11

# the hypothesis refers to the time Mary can do a piece of work, which is also mentioned in the premise
if work_time_hypothesis <= work_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_time_premise'
    label = "contradiction"
else:
    # the premise gives an exact time for Mary to do a piece of work
    # any time greater than 'work_time_premise' contradicts the premise
    label = "entailment"

print(label)
