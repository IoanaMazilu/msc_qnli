# Define variables with representative names for the numerical entities in both inputs
score_1 = 1
score_2 = 2
score_3 = 3
score_4 = 4
score_5 = 5
score_8 = 8

# Extract all quantities as valid numbers (integers or floats)
score_1_premise = 1
score_2_premise = 2
score_3_premise = 3
score_4_premise = 4
score_5_premise = 5
score_8_premise = 8

score_1_hypothesis = 1
score_2_hypothesis = 2
score_3_hypothesis = 3
score_4_hypothesis = 4
score_5_hypothesis = 5
score_8_hypothesis = 8

# Use brief comments to explain what comparison you do between the defined variables
if score_1_premise <= score_1_hypothesis:
    # Check if the hypothesis value contradicts the estimate of more than'score_1_premise'
    label = "contradiction"
elif score_2_premise <= score_2_hypothesis:
    # Check if the hypothesis value contradicts the estimate of more than'score_2_premise'
    label = "contradiction"
elif score_3_premise <= score_3_hypothesis:
    # Check if the hypothesis value contradicts the estimate of more than'score_3_premise'
    label = "contradiction"
elif score_4_premise <= score_4_hypothesis:
    # Check if the hypothesis value contradicts the estimate of more than'score_4_premise'
    label = "contradiction"
elif score_5_premise <= score_5_hypothesis:
    # Check if the hypothesis value contradicts the estimate of more than'score_5_premise'
    label = "contradiction"
elif score_8_premise <= score_8_hypothesis:
    # Check if the hypothesis value contradicts the estimate of more than'score_8_premise'
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
