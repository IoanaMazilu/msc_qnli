# Premise: 9.0 friends were at a restaurant, and they were joined by 7.0 more people and each person ate 4.0 wings.
# Hypothesis: The total amount of wings consumed by the group is 64.0.
# Golden Label: entailment

friends_premise = 9.0
joined_premise = 7.0
wings_premise = 4.0
total_wings_hypothesis = 64.0

# the hypothesis refers to the total amount of wings consumed by the group, which can also be calculated from the premise
# calculate the total number of people and then the total amount of wings consumed in the premise
total_people_premise = friends_premise + joined_premise
total_wings_premise = total_people_premise * wings_premise

if total_wings_hypothesis != total_wings_premise:
    # check if the total amount of wings consumed in the hypothesis contradicts the total amount of wings consumed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

