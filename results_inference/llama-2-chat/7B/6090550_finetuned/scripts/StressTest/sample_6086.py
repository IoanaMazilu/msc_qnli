# the hypothesis is stating the time it takes for Ram and Shyam to do a piece of work together
time_hypothesis = 30

# the premise states the same time
time_premise = 30

# check if the hypothesis time contradicts the premise time
if time_hypothesis!= time_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
