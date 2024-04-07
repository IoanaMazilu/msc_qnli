# Premise: On the first day of her vacation, Louisa traveled 240 miles.
# Hypothesis: On the first day of her vacation, Louisa traveled 340 miles.
# Golden Label: contradiction

miles_traveled_premise = 240
miles_traveled_hypothesis = 340

# the hypothesis is referring to the same distance traveled by Louisa as in the premise
if miles_traveled_hypothesis != miles_traveled_premise:
    # check if the distance traveled in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the distance traveled in the hypothesis does not contradict the distance reported in the premise, we can infer entailment
    label = "entailment"

print(label)

