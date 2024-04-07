# Premise: During a car trip, Maria stopped to rest after she traveled less than 2/2 of the total distance to her destination.
# Hypothesis: During a car trip, Maria stopped to rest after she traveled 1/2 of the total distance to her destination.
# Golden Label: neutral

distance_traveled_premise = 2/2
distance_traveled_hypothesis = 1/2

# the hypothesis talks about the distance Maria traveled during a car trip, which is also referenced in the premise
if distance_traveled_hypothesis > distance_traveled_premise:
    # check if the distance traveled in the hypothesis contradicts the estimate of less than 'distance_traveled_premise'
    label = "contradiction"
elif distance_traveled_hypothesis == distance_traveled_premise:
    # check if the distance traveled in the hypothesis explicitly matches the distance traveled in the premise
    label = "entailment"
else:
    # if the distance traveled in the hypothesis is less than the distance traveled in the premise, it doesn't contradict the information but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

