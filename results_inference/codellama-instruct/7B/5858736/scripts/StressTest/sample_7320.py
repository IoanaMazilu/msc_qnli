# Define variables for the numerical entities in the premise and hypothesis
gym_visits_premise = 2
gym_visits_hypothesis = 2

# Extract all quantities as valid numbers
gym_visits_premise = int(gym_visits_premise)
gym_visits_hypothesis = int(gym_visits_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if gym_visits_hypothesis <= gym_visits_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'gym_visits_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of gym visits
    # Any number of gym visits greater than 'gym_visits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
