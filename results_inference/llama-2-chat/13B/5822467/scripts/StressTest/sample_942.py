gang_size_premise = 8
gang_size_hypothesis = int(input("Enter the number of gang members: "))

# convert the hypothesis to an integer to compare
if gang_size_hypothesis <= 3:
    # the hypothesis is contradictory to the premise, as it implies a smaller gang size
    label = "contradiction"
elif gang_size_premise <= gang_size_hypothesis:
    # the premise implies a smaller gang size, so the hypothesis is neutral
    label = "neutral"
else:
    # the hypothesis implies a larger gang size, which can be entailed from the premise
    label = "entailment"

print(label)
