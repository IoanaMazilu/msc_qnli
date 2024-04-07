# Premise: Stacy has a 63 page history paper due in 3 days.
# Hypothesis: Stacy has a more than 63 page history paper due in 3 days.
# Golden Label: contradiction

paper_length_premise = 63
paper_length_hypothesis = 63
days_due_premise = 3
days_due_hypothesis = 3

# The hypothesis talks about the length of a paper and the due date, both referenced in the premise
if paper_length_hypothesis > paper_length_premise:
    # check if the hypothesis value contradicts the exact length of 'paper_length_premise' 
    label = "contradiction"
elif days_due_hypothesis != days_due_premise:
    # check if the due date in the hypothesis contradicts the due date reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

