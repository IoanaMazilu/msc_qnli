people_premise = 6.0
lemon_heads_per_person_premise = 54.0
total_lemon_heads_premise = people_premise * lemon_heads_per_person_premise

lemon_heads_hypothesis = 327.0

if lemon_heads_hypothesis!= total_lemon_heads_premise:
    # check if the number of lemon heads in the hypothesis contradicts the number of lemon heads from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
