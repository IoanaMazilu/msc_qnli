# define variables for the number of members traveling to each destination
england_france_premise = 6
england_italy_premise = 0
france_italy_premise = 11
england_france_hypothesis = 3
england_italy_hypothesis = 0
france_italy_hypothesis = 11

# check if the hypothesis values contradict the premise ones
if england_france_hypothesis!= england_france_premise:
    label = "contradiction"
elif england_italy_hypothesis!= england_italy_premise:
    label = "contradiction"
elif france_italy_hypothesis!= france_italy_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
