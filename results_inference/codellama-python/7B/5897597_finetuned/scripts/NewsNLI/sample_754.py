people_detained_premise = 939
people_arrested_hypothesis = 939

# the hypothesis mentions the number of people arrested in Turkey, which is also referenced in the premise
if people_detained_premise!= people_arrested_hypothesis:
    # check if the number of people arrested in the hypothesis contradicts the number of people detained in the premise
    label = "contradiction"
else:
    # if the number of people arrested in the hypothesis does not contradict the number of people detained in the premise, we can infer entailment
    label = "entailment"

print(label)
