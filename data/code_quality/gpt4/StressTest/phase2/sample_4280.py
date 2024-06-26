salary_saved_percentage_premise = 10
salary_saved_percentage_hypothesis = 60

# the hypothesis refers to the percentage of salary saved by Kishore, mentioned also in the premise
if salary_saved_percentage_hypothesis != salary_saved_percentage_premise:
    # check if the percentage of salary saved in the hypothesis contradicts with the percentage reported in the premise
    label = "contradiction"

print(label)
