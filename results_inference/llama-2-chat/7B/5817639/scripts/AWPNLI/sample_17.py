picked_pears_premise = [46.0, 47.0, 12.0]
total_picked_pears_hypothesis = 101.0

# compare the number of pears picked by each person in the premise
person_picked_pears_premise = [picked_pears_premise[0], picked_pears_premise[1], picked_pears_premise[2]]

# check if the total number of pears picked in the hypothesis contradicts the total number of pears picked in the premise
if total_picked_pears_hypothesis!= sum(person_picked_pears_premise):
    label = "contradiction"
elif any(person_picked_pears_premise[i] > total_picked_pears_hypothesis for i in range(3)):
    label = "contradiction"
else:
    label = "entailment"

print(label)
