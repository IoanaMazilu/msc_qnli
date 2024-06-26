participants_premise = 6
participants_hypothesis = 2

# The hypothesis refers to the number of participants in the race mentioned in the premise
if participants_hypothesis > participants_premise:
    # Check if the number of participants in the hypothesis contradicts the number of participants reported in the premise
    label = "contradiction"
elif participants_hypothesis < participants_premise:
    # Even though Meg and Bob are among the participants, the hypothesis does not cover all participants of the race in the premise
    label = "neutral"
else:
    # If the hypothesis values do not contradict the premise ones and cover all participants, we can infer entailment
    label = "entailment"

print(label)
