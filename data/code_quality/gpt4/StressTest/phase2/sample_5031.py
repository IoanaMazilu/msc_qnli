avg_shirts_premise = 60
avg_shirts_hypothesis = 40
shirts_purchased = 1

# The hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya, also mentioned in the premise
if avg_shirts_premise + shirts_purchased <= avg_shirts_hypothesis + shirts_purchased:
    # Check if the hypothesis value contradicts the premise for average number of shirts per person after they each purchased a shirt
    label = "contradiction"
elif avg_shirts_hypothesis + shirts_purchased != avg_shirts_premise + shirts_purchased:
    # Check if the average number of shirts in the hypothesis equals the average number of shirts in the premise after each person purchased a shirt
    label = "neutral"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
