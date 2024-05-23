seats_premise = 14.0
people_hypothesis = 85.0

# the hypothesis talks about the number of people that can ride the Ferris wheel, which is also mentioned in the premise
# compute the total number of people that can ride the Ferris wheel from the premise
total_people_premise = seats_premise * 6.0
if total_people_hypothesis!= total_people_premise:
    # check if the number of people in the hypothesis contradicts the number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)