# Premise: Jill invited 37.0 people to her birthday party, and each pizza is divided into 8 equal parts and each person eats 1.0 slice.
# Hypothesis: 6.0 pizzas were eaten.
# Golden Label: contradiction

invited_people_premise = 37.0
pizza_slices_premise = 8.0
slices_per_person_premise = 1.0
pizzas_eaten_hypothesis = 6.0

# the hypothesis refers to the number of pizzas eaten, which is derived from the number of people and slices per pizza in the premise
# compute the total number of pizzas eaten in the premise
total_pizzas_premise = (invited_people_premise * slices_per_person_premise) / pizza_slices_premise
if total_pizzas_premise != pizzas_eaten_hypothesis:
    # check if the number of pizzas eaten in the hypothesis contradicts the number of pizzas eaten from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

