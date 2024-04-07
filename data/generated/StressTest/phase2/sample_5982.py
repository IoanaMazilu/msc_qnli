# Premise: If 25% of all the students at Morse have cars, how many students are in the three lower grades?
# Hypothesis: If less than 35% of all the students at Morse have cars, how many students are in the three lower grades?
# Golden Label: entailment

car_owners_premise = 25
car_owners_hypothesis = 35

# the hypothesis refers to the percentage of car owners among students at Morse, as mentioned in the premise
if car_owners_hypothesis <= car_owners_premise:
    # check if the percentage of car owners stated in the hypothesis contradicts the percentage given in the premise
    label = "contradiction"
else:
    # the premise gives a specific percentage of car owners
    # any percentage greater than 'car_owners_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

