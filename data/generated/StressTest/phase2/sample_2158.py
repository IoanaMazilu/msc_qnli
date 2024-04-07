# Premise: To be considered for “ movie of the year, ” a film must appear in at least less than 4/4 of the top-10-movies lists submitted by the Cinematic Academy’s 775 members.
# Hypothesis: To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 775 members.
# Golden Label: neutral

# defining the numeric entities in the premise and hypothesis
lists_appearance_premise = 4/4
lists_appearance_hypothesis = 1/4
academy_members = 775

# the hypothesis refers to the criteria for the "movie of the year" consideration, mentioned in the premise
if lists_appearance_hypothesis > lists_appearance_premise:
    # check if the number of lists a movie has to appear in (according to the hypothesis) contradicts the number mentioned in the premise
    label = "contradiction"
elif lists_appearance_hypothesis < lists_appearance_premise:
    # if the number of appearances required by the hypothesis is less than the one from the premise, we can infer entailment
    label = "entailment"
else:
    # if none of the above conditions is met, we have a neutral situation
    label = "neutral"

print(label)

