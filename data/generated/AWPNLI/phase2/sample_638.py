# Premise: Jill invited 37.0 people to her birthday party, and each pizza is divided into 8 equal parts and each person eats 1.0 slice.
# Hypothesis: 4.625 pizzas were eaten.
# Golden Label: entailment

people_invited_premise = 37.0
slices_per_pizza_premise = 8
slices_per_person_premise = 1.0
pizzas_eaten_hypothesis = 4.625

# the hypothesis refers to the number of pizzas eaten, which are also referenced in the premise
# compute the total number of pizzas eaten in the premise
pizzas_eaten_premise = people_invited_premise * slices_per_person_premise / slices_per_pizza_premise
if pizzas_eaten_hypothesis != pizzas_eaten_premise:
    # check if the number of pizzas eaten in the hypothesis contradicts the number of pizzas eaten from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

