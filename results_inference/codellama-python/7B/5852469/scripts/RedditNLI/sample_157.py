salary_premise = 100000
salary_hypothesis = 100000

# the hypothesis and premise mention the same salary
if salary_hypothesis!= salary_premise:
    # check if the salary in the hypothesis contradicts the salary in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same salary
    # however, the premise does not link the salary to any specific person, while the hypothesis links the salary to the average American worker
    label = "neutral"

print(label)
