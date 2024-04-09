kiran_age_premise = float(input("Enter Kiran's age: "))
bineesh_age_premise = float(input("Enter Bineesh's age: "))
ratio_premise = float(input("Enter the ratio of Kiran's age to Bineesh's age: "))

kiran_age_hypothesis = float(input("Enter Kiran's age in the hypothesis: "))
bineesh_age_hypothesis = float(input("Enter Bineesh's age in the hypothesis: "))
ratio_hypothesis = float(input("Enter the ratio of Kiran's age to Bineesh's age in the hypothesis: "))

# calculate the difference between Kiran's age and Bineesh's age
difference = abs(bineesh_age_hypothesis - kiran_age_hypothesis)

# check if the difference between the ages in the hypothesis contradicts the premise
if difference > 6:
    label = "contradiction"
# check if the ratio of ages in the hypothesis contradicts the premise
elif ratio_hypothesis!= ratio_premise:
    label = "contradiction"
# if the ages and ratio in the hypothesis do not contradict the premise, we can infer entailment
else:
    label = "entailment"

print(label)
