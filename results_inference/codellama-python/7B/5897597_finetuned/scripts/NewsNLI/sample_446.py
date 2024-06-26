countries_premise = 54
countries_hypothesis = 54

# the hypothesis mentions the number of countries in the Commonwealth, which is also mentioned in the premise
if countries_hypothesis!= countries_premise:
    # check if the number of countries in the hypothesis contradicts the number of countries reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
