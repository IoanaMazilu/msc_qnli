# Premise: If 20% of all the students at Morse have cars, how many students are in the three lower grades?
# Hypothesis: If 50% of all the students at Morse have cars, how many students are in the three lower grades?
# Golden Label: contradiction

car_ownership_premise = 20
car_ownership_hypothesis = 50

# the hypothesis refers to the same situation as the premise, but with a different car ownership proportion
if car_ownership_hypothesis != car_ownership_premise:
    # check if the car ownership percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

