injured_premise = 1500
shelterless_premise = 50000
shelterless_hypothesis = 50000

# the hypothesis mentions the number of people without shelter, which is also mentioned in the premise
if shelterless_hypothesis!= shelterless_premise:
    # check if the number of shelterless people in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of shelterless people in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
