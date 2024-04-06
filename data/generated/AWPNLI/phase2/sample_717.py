# Premise: Jane's mom made 12.0 cinnamon swirls for each person, and there are 3.0 people eating.
# Hypothesis: 40.0 rolls were made in total.
# Golden Label: contradiction

rolls_each_person_premise = 12.0
people_eating_premise = 3.0
total_rolls_hypothesis = 40.0

# the hypothesis refers to the total number of rolls made, which can be calculated from the premise
# compute the total number of rolls made in the premise
total_rolls_premise = rolls_each_person_premise * people_eating_premise
if total_rolls_hypothesis != total_rolls_premise:
    # check if the number of rolls in the hypothesis contradicts the number of rolls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

