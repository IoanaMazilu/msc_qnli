# the number of ways to seat 6 people on a bench
seat_6_people_premise = 7
# the number of people in the hypothesis
people_hypothesis = 7

# if Rohit does not want to sit on the middle seat or at either end, then the number of ways to seat 6 people on a bench is also the number of ways to seat 7 people on a bench
# the hypothesis talks about the same scenario as the premise, but with one more person
if seat_6_people_premise == people_hypothesis:
    label = "entailment"
else:
    label = "contradiction"

print(label)
