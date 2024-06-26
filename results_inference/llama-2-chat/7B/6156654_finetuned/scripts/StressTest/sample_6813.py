# calculate the percentage of students with cars in the premise
car_percentage_premise = 18 / 100

# calculate the percentage of students with cars in the hypothesis
car_percentage_hypothesis = 48 / 100

# if the percentage of students with cars in the hypothesis contradicts the percentage in the premise, then the relation is contradiction
if car_percentage_hypothesis <= car_percentage_premise:
    relation = "contradiction"
elif car_percentage_hypothesis > car_percentage_premise:
    relation = "entailment"
else:
    relation = "neutral"

print(relation)
