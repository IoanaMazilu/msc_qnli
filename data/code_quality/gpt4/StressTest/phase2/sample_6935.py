old_job_pay_premise = 75000
old_job_pay_hypothesis = 75000
new_job_base_pay_premise = 45000
new_job_base_pay_hypothesis = 45000
new_job_commission_premise = 15
new_job_commission_hypothesis = 15

# the hypothesis talks about the same pay and commission rates as the premise
if old_job_pay_hypothesis != old_job_pay_premise:
    # check if the old job pay in the hypothesis contradicts the old job pay reported in the premise
    label = "contradiction"
elif new_job_base_pay_hypothesis != new_job_base_pay_premise:
    # check if the new job base pay in the hypothesis contradicts the new job base pay reported in the premise
    label = "contradiction"
elif new_job_commission_hypothesis > new_job_commission_premise:
    # check if the new job commission in the hypothesis contradicts the new job commission reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
