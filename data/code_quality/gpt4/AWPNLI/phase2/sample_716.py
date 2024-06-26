swirls_per_person_premise = 12.0
people_eating_premise = 3.0
total_swirls_hypothesis = 36.0

# the hypothesis refers to the total number of swirls, which is related to the number of swirls per person and the number of people eating in the premise
# compute the total number of swirls in the premise
total_swirls_premise = swirls_per_person_premise * people_eating_premise
if total_swirls_hypothesis != total_swirls_premise:
    # check if the total number of swirls in the hypothesis contradicts the total number of swirls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
