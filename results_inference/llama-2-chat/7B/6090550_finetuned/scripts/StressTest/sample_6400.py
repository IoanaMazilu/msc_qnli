# defining the variables
miami_passengers_premise = 8/2
miami_passengers_hypothesis = 1/2
kennedy_passengers_premise = 8/2
kennedy_passengers_hypothesis = 1/2
logan_passengers_premise = 4
logan_passengers_hypothesis = 4

# the hypothesis refers to the number of passengers that used Miami Airport, which is also mentioned in the premise
if miami_passengers_hypothesis!= miami_passengers_premise:
    # check if the number of passengers that used Miami Airport in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif kennedy_passengers_hypothesis!= kennedy_passengers_premise or logan_passengers_hypothesis!= logan_passengers_premise:
    # check if the number of passengers that used Kennedy Airport or Logan Airport in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
