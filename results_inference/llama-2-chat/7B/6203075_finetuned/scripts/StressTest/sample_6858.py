miles_walked_premise = 4
miles_walked_hypothesis = 3
walking_time_premise = 1.25
walking_time_hypothesis = 1.25

# the hypothesis refers to the distance and time Jack walked, which are also mentioned in the premise
if miles_walked_hypothesis <= miles_walked_premise:
    # check if the hypothesis value contradicts the distance Jack walked in the premise
    label = "contradiction"
elif walking_time_hypothesis!= walking_time_premise:
    # check if the time Jack walked in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
