miami_passengers_premise = 8/2
miami_passengers_hypothesis = 1/2
kennedy_passengers_premise = 1
kennedy_passengers_hypothesis = 1
logan_passengers_premise = 4
logan_passengers_hypothesis = 4

# the hypothesis refers to the number of passengers that used Miami, Kennedy and Logan airports, mentioned in the premise
if miami_passengers_hypothesis > miami_passengers_premise:
    # check if the estimate of'miami_passengers_hypothesis' contradicts the number of Miami passengers in the premise
    label = "contradiction"
elif kennedy_passengers_hypothesis!= kennedy_passengers_premise:
    # check if the number of Kennedy passengers in the hypothesis contradicts the number of Kennedy passengers reported in the premise
    label = "contradiction"
elif logan_passengers_hypothesis!= logan_passengers_premise:
    # check if the number of Logan passengers in the hypothesis contradicts the number of Logan passengers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
