cleaning_time_premise = 6
cleaning_time_hypothesis = 5

# the hypothesis refers to the cleaning time mentioned in the premise
if cleaning_time_hypothesis == cleaning_time_premise:
    # check if the cleaning time in the hypothesis matches the cleaning time in the premise
    label = "entailment"
elif cleaning_time_hypothesis!= cleaning_time_premise:
    # check if the cleaning time in the hypothesis contradicts the cleaning time in the premise
    label = "contradiction"

print(label)
