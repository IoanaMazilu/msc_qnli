# Premise: Two people remained unaccounted for from the SuperFerry 9 vessel carrying 968 people, according to the Philippine Coast Guard.
# Hypothesis: Two people are missing, according to coast guard.
# Golden Label: entailment

missing_people_premise = 2
missing_people_hypothesis = 2

# the hypothesis mentions the number of missing people according to the coast guard, which is also referenced in the premise
if missing_people_hypothesis != missing_people_premise:
    # check if the number of missing people in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of missing people in the hypothesis does not contradict the number reported in the premise, we can infer entailment
    label = "entailment"

print(label)

