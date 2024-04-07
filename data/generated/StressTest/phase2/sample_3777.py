# Premise: While driving from City A to City B, Jim drives at a constant speed of 40 miles per hour.
# Hypothesis: While driving from City A to City B, Jim drives at a constant speed of less than 70 miles per hour.
# Golden Label: entailment

speed_premise = 40
speed_hypothesis = 70

# Hypothesis is referring to the speed Jim drove from City A to City B, which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # Checking if the speed in the hypothesis contradicts the speed stated in the premise
    label = "contradiction"
elif speed_hypothesis > speed_premise:
    # If speed in the hypothesis is more than the premise, it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # If none of the above conditions are true, then the speed in the hypothesis is the same as the premise, implying entailment
    label = "entailment"

print(label)

