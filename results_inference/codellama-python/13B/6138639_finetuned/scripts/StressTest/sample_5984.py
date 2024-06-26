car_percentage_premise = 25
car_percentage_hypothesis = 85

# the hypothesis talks about the percentage of students with cars at Morse, referenced also in the premise
if car_percentage_hypothesis!= car_percentage_premise:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are about the same percentage of students with cars
    # but the premise does not provide any information about the total number of students
    # so we cannot infer entailment or contradiction
    label = "neutral"

print(label)
