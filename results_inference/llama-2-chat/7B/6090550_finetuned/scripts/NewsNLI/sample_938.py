parts_manufactured_premise = 80
parts_manufactured_hypothesis = 80

# the hypothesis mentions the percentage of parts manufactured in the U.S. for a specific type of vehicles, which is also mentioned in the premise
if parts_manufactured_hypothesis!= parts_manufactured_premise:
    # check if the percentage of parts manufactured in the U.S. in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
