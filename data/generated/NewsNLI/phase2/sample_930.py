# Premise: In truth, Argentina were far from their best against the World Cup debutantes Bosnia and Herzegovina despite going 1-0 up thanks to the quickest goal at the World Cup to date.
# Hypothesis: Messi's strike lifts Argentina to a 2-1 win over Bosnia and Herzegovina.
# Golden Label: neutral

argentina_goals_premise = 1
argentina_goals_hypothesis = 2
bosnia_goals_premise = 0
bosnia_goals_hypothesis = 1

# the hypothesis mentions Argentina's final score and Bosnia and Herzegovina's final score, which are not mentioned in the premise
# the premise only states that Argentina were up 1-0 at some point in the match
if argentina_goals_hypothesis != argentina_goals_premise:
    # check if the final score of Argentina in the hypothesis contradicts the score mentioned in the premise
    label = "contradiction"
elif bosnia_goals_hypothesis != bosnia_goals_premise:
    # check if the final score of Bosnia and Herzegovina from the hypothesis contradicts the score mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
