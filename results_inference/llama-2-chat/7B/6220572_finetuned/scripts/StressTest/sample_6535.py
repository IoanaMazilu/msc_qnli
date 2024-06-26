miami_airport_premise = 7/3
miami_airport_hypothesis = 1/3
kennedy_airport_premise = 4
logan_airport_premise = 4

# the hypothesis talks about the number of passengers at Miami Airport, referenced also in the premise
if miami_airport_hypothesis!= miami_airport_premise:
    # check if the hypothesis value contradicts the number of passengers at Miami Airport reported in the premise
    label = "contradiction"
elif kennedy_airport_hypothesis!= kennedy_airport_premise:
    # check if the number of passengers at Kennedy Airport in the hypothesis contradicts the number of passengers at Kennedy Airport reported in the premise
    label = "contradiction"
elif logan_airport_hypothesis!= logan_airport_premise:
    # check if the number of passengers at Logan Airport in the hypothesis contradicts the number of passengers at Logan Airport reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
