# Premise: More than 1.2 million people have since viewed it.
# Hypothesis: Over 1.2 million people have viewed it on YouTube.
# Golden Label: entailment

viewers_premise = 1.2e6
viewers_hypothesis = 1.2e6

# the hypothesis mentions the number of video views, which is also referenced in the premise
# however, the hypothesis specifies that these views were on YouTube, which cannot be entailed from the premise
label = "neutral"

print(label)

