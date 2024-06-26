teams_premise = 5
teams_hypothesis = 2

# the hypothesis refers to the number of teams in a match mentioned in the premise
if teams_hypothesis >= teams_premise:
    # check if the number of teams in the hypothesis contradicts the estimate of less than 'teams_premise'
    label = "contradiction"
elif teams_hypothesis < teams_premise:
    # any number of teams less than 'teams_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
