# Premise: 4320 among John, Jose & Binoy in the ration 2:4:6.
# Hypothesis: more than 3320 among John, Jose & Binoy in the ration 2:4:6.
# Golden Label: entailment

total_amount_premise = 4320
total_amount_hypothesis = 3320

# The hypothesis talks about the total amount among John, Jose & Binoy, which is also mentioned in the premise
if total_amount_premise < total_amount_hypothesis:
    # Check if the total amount in the hypothesis contradicts the total amount mentioned in the premise
    label = "contradiction"
elif total_amount_premise == total_amount_hypothesis:
    # If the total amount in the hypothesis equals the total amount in the premise, it is entailment
    label = "entailment"
else:
    # If the total amount in the hypothesis is less than the total amount in the premise, it does not contradict but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

