# Premise: John alone cleans the entire house in 6 hours.
# Hypothesis: John alone cleans the entire house in more than 1 hours.
# Golden Label: entailment

cleaning_time_premise = 6
cleaning_time_hypothesis = 1

# the hypothesis talks about John's cleaning time, which is also mentioned in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the hypothesis value contradicts the exact cleaning time 'cleaning_time_premise' given in the premise
    label = "contradiction"
elif cleaning_time_hypothesis != cleaning_time_premise:
    # the premise gives an exact cleaning time
    # any cleaning time different than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

