# Premise: There are 300 seniors at Morse High School, and 50% of them have cars.
# Hypothesis: There are less than 600 seniors at Morse High School, and 50% of them have cars.
# Golden Label: entailment

seniors_premise = 300
seniors_hypothesis = 600
seniors_with_cars_premise = 0.50 * seniors_premise
seniors_with_cars_hypothesis = 0.50 * seniors_hypothesis

# the hypothesis refers to the number of seniors and the percentage of those with cars, both mentioned in the premise
if seniors_hypothesis < seniors_premise:
    # check if the number of seniors in the hypothesis contradicts the number of seniors reported in the premise
    label = "contradiction"
elif seniors_with_cars_hypothesis != seniors_with_cars_premise:
    # check if the number of seniors with cars in the hypothesis contradicts the number of seniors with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

