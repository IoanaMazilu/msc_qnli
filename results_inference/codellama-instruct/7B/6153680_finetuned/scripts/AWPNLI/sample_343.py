wood_gathered_premise = 80.0
sacks_filled_premise = 6.0
wood_per_sack_premise = 20.0

# the hypothesis refers to the number of sacks filled and the total number of pieces of wood gathered, which are also mentioned in the premise
# compute the total number of pieces of wood gathered in the premise
total_wood_gathered_premise = wood_gathered_premise / sacks_filled_premise * wood_per_sack_premise

# the hypothesis states that they were able to fill 6.0 sacks if they gathered 80.0 pieces of wood
# compute the total number of pieces of wood gathered in the hypothesis
total_wood_gathered_hypothesis = wood_gathered_premise

# check if the total number of pieces of wood gathered in the hypothesis contradicts the total number of pieces of wood gathered in the premise
if total_wood_gathered_hypothesis!= total_wood_gathered_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
