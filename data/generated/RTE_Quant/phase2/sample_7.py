# Premise: The first Windows Challenge was held in 2004, consisting of less than 30 teams within the United States. In 2005, it was opened to the rest of the world. 278 teams from all over the world participated.
# Hypothesis: 278 teams from all over the world participated in the first Windows Challenge.
# Golden Label: neutral

first_challenge_year_premise = 2004
teams_in_US_premise = 30
second_challenge_year_premise = 2005
world_teams_premise = 278
first_challenge_year_hypothesis = 2004
world_teams_hypothesis = 278

# the hypothesis talks about the number of teams from all over the world in the first challenge, which contradicts the premise
if first_challenge_year_hypothesis == first_challenge_year_premise and world_teams_hypothesis >= teams_in_US_premise:
    # check if the number of teams in the first challenge contradicts the number of teams in the premise
    label = "contradiction"
else:
    # otherwise, the relation is neutral
    label = "neutral"

print(label)

