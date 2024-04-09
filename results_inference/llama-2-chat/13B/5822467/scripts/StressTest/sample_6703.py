kiran_age_premise = float(input("Enter Kiran's age in the premise: "))
bineesh_age_premise = float(input("Enter Bineesh's age in the premise: "))
age_diff_premise = bineesh_age_premise - kiran_age_premise
ratio_premise = float(input("Enter the ratio of their ages in the premise: "))

kiran_age_hypothesis = float(input("Enter Kiran's age in the hypothesis: "))
bineesh_age_hypothesis = float(input("Enter Bineesh's age in the hypothesis: "))
age_diff_hypothesis = bineesh_age_hypothesis - kiran_age_hypothesis
ratio_hypothesis = float(input("Enter the ratio of their ages in the hypothesis: "))

# Check if the hypothesis values and estimates do not contradict the premise ones
if age_diff_premise == age_diff_hypothesis and ratio_premise == ratio_hypothesis:
    # If the hypothesis values and estimates are consistent with the premise values and estimates, we can infer entailment
    print("entailment")
else:
    # If the hypothesis values and estimates contradict the premise values and estimates, we can infer contradiction
    print("contradiction")
