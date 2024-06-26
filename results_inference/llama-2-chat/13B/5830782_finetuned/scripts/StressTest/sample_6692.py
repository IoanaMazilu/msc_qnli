air_travel_premise = 1800
air_travel_hypothesis = 7800

# the hypothesis talks about the distance travelled by air, which is also mentioned in the premise
if air_travel_hypothesis!= air_travel_premise:
    # check if the distance travelled by air in the hypothesis contradicts the distance travelled by air reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
