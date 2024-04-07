# Premise: John was thrice as old as Tom 6 years ago.
# Hypothesis: John was thrice as old as Tom more than 2 years ago.
# Golden Label: entailment

years_premise = 6
years_hypothesis = 2

# the hypothesis refers to a time period when John was thrice as old as Tom, which is also mentioned in the premise
if years_premise < years_hypothesis:
    # check if the time period in the hypothesis contradicts the time period in the premise
    label = "contradiction"
elif years_premise > years_hypothesis:
    # check if the time period in the hypothesis is less than the time period in the premise
    label = "entailment"
else:
    # if the time period in the hypothesis is the same as the time period in the premise, we can infer neutrality
    label = "neutral"

print(label)

