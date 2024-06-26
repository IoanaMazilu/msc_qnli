miami_airport_ratio_premise = 7/3
logan_airport_ratio_premise = 4

miami_airport_ratio_hypothesis = 1/3
logan_airport_ratio_hypothesis = 4

# the hypothesis refers to the ratio of passengers at Miami Airport, which is also mentioned in the premise
if miami_airport_ratio_hypothesis!= miami_airport_ratio_premise:
    # check if the ratio of Miami Airport in the hypothesis contradicts the ratio of Miami Airport in the premise
    label = "contradiction"
elif logan_airport_ratio_hypothesis!= logan_airport_ratio_premise:
    # check if the ratio of Logan Airport in the hypothesis contradicts the ratio of Logan Airport in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
