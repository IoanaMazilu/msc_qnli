# Premise: Wendy's old washing machine could only wash 8.0 pieces of clothing at a time, and she had to wash 39.0 shirts and 33.0 sweaters.
# Hypothesis: She would have 6.0 loads to do.
# Golden Label: contradiction

clothes_per_load_premise = 8.0
shirts_premise = 39.0
sweaters_premise = 33.0
loads_hypothesis = 6.0

# the hypothesis refers to the number of loads, calculated based on the number of clothes and the capacity of the washing machine
# compute total clothes and loads in the premise
total_clothes_premise = shirts_premise + sweaters_premise
loads_premise = total_clothes_premise / clothes_per_load_premise

if loads_hypothesis != round(loads_premise):
    # check if the number of loads in the hypothesis contradicts the number of loads calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

