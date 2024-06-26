england_france_premise = 8
england_france_hypothesis = 6
italy_premise = 0
italy_hypothesis = 0

# the hypothesis refers to the number of members that traveled to England and France, which is also mentioned in the premise
if england_france_hypothesis >= england_france_premise:
    # check if the number of members in the hypothesis contradicts the premise
    label = "contradiction"
elif italy_hypothesis!= italy_premise:
    # check if the number of members that traveled to Italy in the hypothesis contradicts the number of members in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
