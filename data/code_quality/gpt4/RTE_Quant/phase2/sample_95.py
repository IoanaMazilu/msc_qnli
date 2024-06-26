temp_help_firms_jobs_premise = 32000
edu_health_services_jobs_premise = 13000
total_jobs_premise = temp_help_firms_jobs_premise + edu_health_services_jobs_premise
service_industries_jobs_hypothesis = 46000

# the hypothesis talks about the total jobs added in service industries
# we compare the total jobs mentioned in the hypothesis with the total jobs calculated from the premise
if service_industries_jobs_hypothesis != total_jobs_premise:
    # check if the total jobs in the hypothesis contradicts the total jobs calculated from the premise
    label = "contradiction"
else:
    # if the total jobs in the hypothesis does not contradict the total jobs calculated from the premise, we can infer entailment
    label = "entailment"

print(label)
