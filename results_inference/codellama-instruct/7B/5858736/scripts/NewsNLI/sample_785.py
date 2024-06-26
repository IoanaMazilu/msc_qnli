# Define variables for the numerical entities in the premise and hypothesis
years_played_premise = 12
teams_played_premise = 4
leagues_played_premise = 2

years_played_hypothesis = 12
teams_played_hypothesis = 1
leagues_played_hypothesis = 1

# Extract all quantities as valid numbers
years_played_premise = float(years_played_premise)
teams_played_premise = float(teams_played_premise)
leagues_played_premise = float(leagues_played_premise)

years_played_hypothesis = float(years_played_hypothesis)
teams_played_hypothesis = float(teams_played_hypothesis)
leagues_played_hypothesis = float(leagues_played_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if years_played_hypothesis!= years_played_premise:
    # Check if the number of years played in the hypothesis contradicts the number of years played in the premise
    label = "contradiction"
elif teams_played_hypothesis!= teams_played_premise:
    # Check if the number of teams played in the hypothesis contradicts the number of teams played in the premise
    label = "contradiction"
elif leagues_played_hypothesis!= leagues_played_premise:
    # Check if the number of leagues played in the hypothesis contradicts the number of leagues played in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
