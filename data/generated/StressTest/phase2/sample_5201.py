# Premise: Dana borrows 4000 pounds annually for her college education.
# Hypothesis: Dana borrows 8000 pounds annually for her college education.
# Golden Label: contradiction

annual_borrow_premise = 4000
annual_borrow_hypothesis = 8000

# the hypothesis refers to the amount of money Dana borrows each year as stated in the premise
if annual_borrow_hypothesis != annual_borrow_premise:
    # check if the amount of money borrowed annually in the hypothesis contradicts the one stated in the premise
    label = "contradiction"
else:
    # if the values are the same, the hypothesis is entailed by the premise
    label = "entailment"

print(label)

