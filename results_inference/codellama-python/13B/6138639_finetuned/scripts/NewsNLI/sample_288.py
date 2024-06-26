injured_premise = 1500
injured_hypothesis = 0
shelter_premise = 50000
shelter_hypothesis = 50000

# the hypothesis mentions the number of people without shelter in Italy, which is also mentioned in the premise
# however, the hypothesis does not mention the number of injured people, which is mentioned in the premise
if shelter_hypothesis!= shelter_premise:
    # check if the number of people without shelter in the hypothesis contradicts the number of people without shelter in the premise
    label = "contradiction"
elif injured_hypothesis!= injured_premise:
    # check if the number of injured people from the hypothesis contradicts the number of injured people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
