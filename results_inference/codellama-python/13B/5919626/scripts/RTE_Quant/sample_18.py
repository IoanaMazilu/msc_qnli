number_of_people_premise = 200000
number_of_people_hypothesis = 200000

# the hypothesis talks about the number of people killed in the air attack in the Darfur region, which is also mentioned in the premise
if number_of_people_hypothesis!= number_of_people_premise:
    # check if the number of people killed in the air attack in the Darfur region in the hypothesis contradicts the number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
