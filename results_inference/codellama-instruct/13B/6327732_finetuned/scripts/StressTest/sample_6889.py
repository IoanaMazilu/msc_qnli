num_people_premise = 8
num_people_hypothesis = 6

# the hypothesis refers to the number of people that can be seated on a bench
# the premise mentions that one person, Rohit, does not want to sit on the middle seat or at either end
# the hypothesis value is less than the premise value, so we can infer contradiction
if num_people_hypothesis >= num_people_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
