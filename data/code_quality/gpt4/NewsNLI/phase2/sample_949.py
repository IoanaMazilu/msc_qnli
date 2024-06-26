people_killed_premise = 3
people_killed_hypothesis = 7

# the hypothesis mentions the total number of people killed in North Carolina, which likely includes the number of people killed in Raleigh
# to check the assertion made in the hypothesis, we compare the number of people killed in the premise with the number from the hypothesis
if people_killed_premise > people_killed_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)
