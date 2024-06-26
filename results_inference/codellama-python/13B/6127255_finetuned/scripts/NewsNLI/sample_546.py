relegation_premise = 10
relegation_hypothesis = 10

# the hypothesis mentions the number of places Maldonado was relegated, which is also mentioned in the premise
if relegation_hypothesis!= relegation_premise:
    # check if the relegation in the hypothesis contradicts the relegation reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
