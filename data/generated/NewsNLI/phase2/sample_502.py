# Premise: Beason is about 45 miles northeast of Springfield, Illinois.
# Hypothesis: Killings occurred in Beason, Illinois, about 45 miles northeast of Springfield.
# Golden Label: neutral

distance_premise = 45
distance_hypothesis = 45

# the hypothesis mentions the distance of Beason from Springfield, Illinois, which is also mentioned in the premise
# however, the hypothesis introduces the piece of information about killings in Beason, which cannot be entailed from the premise
label = "neutral"

print(label)

