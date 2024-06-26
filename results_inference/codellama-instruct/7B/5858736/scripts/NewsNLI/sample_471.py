# Define variables with representative names for the numerical entities in both inputs
games_played_premise = 1
goals_scored_premise = 5
goals_conceded_premise = 1
home_advantage_premise = 1

games_played_hypothesis = 1
goals_scored_hypothesis = 5
goals_conceded_hypothesis = 1
home_advantage_hypothesis = 1

# Extract all quantities as valid numbers (integers or floats)
games_played_premise = int(games_played_premise)
goals_scored_premise = int(goals_scored_premise)
goals_conceded_premise = int(goals_conceded_premise)
home_advantage_premise = int(home_advantage_premise)

games_played_hypothesis = int(games_played_hypothesis)
goals_scored_hypothesis = int(goals_scored_hypothesis)
goals_conceded_hypothesis = int(goals_conceded_hypothesis)
home_advantage_hypothesis = int(home_advantage_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if goals_scored_hypothesis!= goals_scored_premise:
    # check if the number of goals scored in the hypothesis contradicts the number of goals scored in the premise
    label = "contradiction"
elif goals_conceded_hypothesis!= goals_conceded_premise:
    # check if the number of goals conceded in the hypothesis contradicts the number of goals conceded in the premise
    label = "contradition"
elif home_advantage_hypothesis!= home_advantage_premise:
    # check if the home advantage in the hypothesis contradicts the home advantage in the premise
    label = "contradition"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
