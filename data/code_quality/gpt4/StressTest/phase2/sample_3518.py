science_students_premise = 100
science_students_hypothesis = 100
local_science_students_premise = 0.25 * science_students_premise
local_science_students_hypothesis = 0.55 * science_students_hypothesis

commerce_students_premise = 120
commerce_students_hypothesis = 120
local_commerce_students_premise = 0.85 * commerce_students_premise
local_commerce_students_hypothesis = 0.85 * commerce_students_hypothesis

# the hypothesis talks about the proportion of local students in the Science and Commerce departments, referenced also in the premise
if local_science_students_hypothesis != local_science_students_premise:
    # check if the hypothesis value contradicts the estimate of 'local_science_students_premise'
    label = "contradiction"
elif local_commerce_students_hypothesis != local_commerce_students_premise:
    # check if the hypothesis value contradicts the estimate of 'local_commerce_students_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
