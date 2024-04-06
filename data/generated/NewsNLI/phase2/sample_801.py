# Premise: Meanwhile, tournament favorite Ivory Coast came from two goals down to draw 2-2 with Algeria in Rustenburg.
# Hypothesis: Ivory Coast tops group following 2-2 draw against Algeria.
# Golden Label: neutral

ivory_coast_score_premise = 2
algeria_score_premise = 2
ivory_coast_score_hypothesis = 2
algeria_score_hypothesis = 2

# the hypothesis mentions the score of the match between Ivory Coast and Algeria, which is also mentioned in the premise
# however, the hypothesis provides additional information about Ivory Coast topping the group, which cannot be entailed from the premise
label = "neutral"

print(label)

