total_people_premise = 60
people_iceland_premise = 35
people_norway_premise = 23

total_people_hypothesis = 40
people_iceland_hypothesis = 35
people_norway_hypothesis = 23

# the hypothesis talks about the number of people who have visited Iceland and Norway, which are also mentioned in the premise
if people_iceland_hypothesis!= people_iceland_premise:
    # check if the number of people who visited Iceland in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif people_norway_hypothesis!= people_norway_premise:
    # check if the number of people who visited Norway in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
