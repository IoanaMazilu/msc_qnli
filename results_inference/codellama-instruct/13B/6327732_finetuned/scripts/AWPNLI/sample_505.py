people_premise = 6.0
lemon_heads_per_person_premise = 54.0
total_lemon_heads_premise = people_premise * lemon_heads_per_person_premise

lemon_heads_hypothesis = 327.0

if lemon_heads_hypothesis!= total_lemon_heads_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
