# Premise: If Anne’s speed were doubled, they could clean their house in 3 hours working at their respective rates.
# Hypothesis: If Anne’s speed were doubled, they could clean their house in 2 hours working at their respective rates.
# Golden Label: contradiction

cleaning_time_premise = 3
cleaning_time_hypothesis = 2

# both the premise and hypothesis discuss the hypothetical situation of Anne's speed doubling and how it would affect the cleaning time
if cleaning_time_hypothesis > cleaning_time_premise:
    # check if the hypothesis cleaning time contradicts with the premise's estimated cleaning time
    label = "contradiction"
elif cleaning_time_hypothesis == cleaning_time_premise:
    # check if the hypothesis cleaning time matches exactly with the premise's estimated cleaning time
    label = "entailment"
else:
    # the premise gives only an estimate for the cleaning time
    # any cleaning time less than 'cleaning_time_premise' is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

