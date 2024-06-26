race_length_premise = 100
race_length_hypothesis = 400

# the hypothesis talks about the length of the race that Adam watched, also referenced in the premise
if race_length_hypothesis != race_length_premise:
    # check if the length of the race in the hypothesis contradicts the length of the race reported in the premise
    label = "contradiction"
else:
    # the length of the race in the hypothesis matches the length reported in the premise and can be inferred as entailment
    label = "entailment"

print(label)