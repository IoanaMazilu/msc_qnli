# Premise: 1 beat sixth-seed Andy Murray 7-6 (5) 6-7 (4) 6-3 6-0 in a contentious slugfest in Melbourne, he become only the second man to claim five Australian Open titles.
# Hypothesis: Djokovic becomes the second man to claim five Oz titles.
# Golden Label: neutral

titles_premise = 5
titles_hypothesis = 5

# the hypothesis mentions the number of Australian Open titles won, which is also referenced in the premise
if titles_hypothesis == titles_premise:
    # check if the number of titles in the hypothesis matches the number of titles in the premise
    label = "entailment"
else:
    # if the number of titles from the hypothesis does not match the number of titles in the premise, we infer a contradiction
    label = "contradiction"

print(label)

