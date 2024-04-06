# Premise: New voters also are less likely to be Republicans (27 percent, compared with 36 percent of repeat voters) and more apt to be liberals (28 percent vs. 17 percent).
# Hypothesis: Among likely voters in this survey, 36 percent are Democrats.
# Golden Label: neutral

republicans_new_voters_premise = 27
republicans_repeat_voters_premise = 36
liberals_new_voters_premise = 28
liberals_repeat_voters_premise = 17

democrats_hypothesis = 36

# the hypothesis talks about the percentage of democrats, which is not referenced in the premise (only republicans and liberals are mentioned)
# the hypothesis cannot be entailed from the premise, since the percentage of democrats is unknown.
label = "neutral"

print(label)

