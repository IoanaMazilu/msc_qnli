# Premise: Between 20 and 30 people were trapped in the casino because of debris from the explosions, said Cmdr.
# Hypothesis: Up to 30 people thought trapped in the casino because of debris.
# Golden Label: entailment

min_people_premise = 20
max_people_premise = 30
max_people_hypothesis = 30

# the hypothesis mentions the possible maximum number of people trapped which is also mentioned in the premise
# however, the hypothesis does not specify the minimum number of people trapped
if max_people_hypothesis > max_people_premise:
    # check if the maximum number of people in the hypothesis contradicts the maximum number in the premise
    label = "contradiction"
else:
    # if the maximum number of people in the hypothesis does not contradict the maximum number in the premise, we infer neutral
    label = "neutral"

print(label)

