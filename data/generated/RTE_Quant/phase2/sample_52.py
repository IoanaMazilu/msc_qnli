# Premise: Last week, the attorney general of Connecticut, Richard Blumenthal, turned up the pressure when he said the state would no longer extend its insurance plan for its 188,000 employees to cover prescriptions filled at Wal-Mart unless the chain agreed to stock the pills.
# Hypothesis: The attorney general of Connecticut, Richard Blumenthal has 188,000 employees.
# Golden Label: neutral

employees_premise = 188000
employees_hypothesis = 188000

# the hypothesis states that Richard Blumenthal has 188,000 employees, while the premise states that the state has 188,000 employees
# the hypothesis cannot be entailed from the premise, as the employer in the premise (the state) is not the same as in the hypothesis (Richard Blumenthal)
label = "contradiction"

print(label)

