# Premise: The group includes 19 women and five men.
# Hypothesis: The mostly middle-aged group includes 19 women and five men.
# Golden Label: neutral

women_premise = 19
men_premise = 5
women_hypothesis = 19
men_hypothesis = 5

# the hypothesis mentions the number of women and men in the group, which are also referenced in the premise
# however, the hypothesis refers to the group as mostly middle-aged, which cannot be entailed from the premise
label = "neutral"

print(label)

