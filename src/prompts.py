from typing import Optional

from langchain.prompts import PromptTemplate

# instruction prompt for datasets with entailment + contradiction + neutral labels
# template_ecn = """
# You need to reason about weather a hypothesis entails, contradicts or is neutral with respect to a premise, by
# generating Python scripts. The scripts should classify the relation between the hypothesis and premise based on the
# quantitative and textual information mentioned in them. All the quantities and textual details in the hypothesis should
# be entailed by the information in the premise. First, manually extract all the individual quantities from both of the inputs,
# as valid numbers. Use the variable name to describe what the quantity measures, based on the context. Then, define a
# Python function that takes the extracted quantities as arguments. Within the function, first check if the hypothesis
# facts or quantities contradict the premise ones. If there is no contradiction, check if all the hypothesis quantities
# and details entail the premise information. If you need to, use these quantities to perform computations based on the
# context of the premise and hypothesis. Finally, compare the resulting variables to determine the relationship. The
# comparison should use operators inferred from the context and quantifiers, if any are used. If the comparison indicates
# entailment, return True; for contradiction return False, and for neutrality return None. Remember to include brief
# comments in the script to explain each step of the reasoning process. To illustrate, consider the following examples:
#
# {examples}
#
# Your turn now:
# Premise: {premise}
# Hypothesis: {hypothesis}
# Answer:
# """
#
# # instruction prompt for datasets with entailment + contradiction labels
# template_ec = """
# You need to reason about weather a hypothesis entails or contradicts a premise, by generating Python scripts. The
# scripts should classify the relation between the hypothesis and premise based on the quantitative and textual
# information mentioned in them. All the quantities and textual details in the hypothesis should be entailed by the
# information in the premise. First, manually extract all the individual quantities from both of the inputs, as valid
# numbers. Use the variable name to describe what the quantity measures, based on the context. Then, define a Python
# function that takes the extracted quantities as arguments. Within the function, use these quantities to perform
# computations based on the context of the premise and hypothesis. Finally, compare the resulting variables to determine
# the relationship. If the comparison indicates entailment, return True; for contradiction return False. Remember to
# include brief comments in the script to explain each step of the reasoning process. To illustrate, consider the
# following examples:
#
# {examples}
#
# Your turn now:
# Premise: {premise}
# Hypothesis: {hypothesis}
# Answer:
# """
#
# # instruction prompt for datasets with entailment + neutral labels
# template_en = """
# You need to reason about weather a hypothesis entails or is neutral with respect to a premise, by generating Python
# scripts. The scripts should classify the relation between the hypothesis and premise based on the quantitative and
# textual information mentioned in them. All the quantities and textual details in the hypothesis should entail
# the information in the premise. Pay attention to the wording of the hypothesis, as it may indicate details which cannot
# be entailed from the premise directly. First, manually extract all the individual quantities from both of the inputs, as valid
# numbers. Use the variable name to describe what the quantity measures, based on the context. Then, define a Python
# function that takes the extracted quantities as arguments. Within the function, reason as to weather the quantities in
# the hypothesis refer to the same entities as those in the premise. If they don't, then return None for neutrality.
# If they do, compare them and return True if the hypothesis values entail those in the premise, or None otherwise.
# To illustrate, consider the following examples:
#
# {examples}
#
# Your turn now:
# Premise: {premise}
# Hypothesis: {hypothesis}
# Answer:
# """
#
# # FEW-SHOT EXAMPLES FOR EACH DATASET
#
# newsnli_examples = """START_EXAMPLE
# Premise: Besides 100 small-breed dogs, 57 large-breed dogs were rescued in over a week.
# Hypothesis: 100 small-breed dogs and 57 large-breed dogs were rescued.
# Answer:
# ```python
# small_tale_dogs_premise = 100
# large_tale_dogs_premise = 57
# small_tale_dogs_hypothesis = 100
# small_tale_dogs_hypothesis = 57
#
# def entailment_or_neutral(small_tale_dogs_premise, large_tale_dogs_premise, small_tale_dogs_hypothesis, small_tale_dogs_hypothesis):
#     # the number or rescued dogs of small or large scale in the hypothesis are also referenced in the premise
#     # check if the quantities in the hypothesis entail those in the premise, by checking if they are equal
#     if small_tale_dogs_premise == small_tale_dogs_hypothesis and large_tale_dogs_premise == small_tale_dogs_hypothesis:
#         return True
#     else:
#         return None
#
# print(entailment_or_neutral(small_tale_dogs_premise, large_tale_dogs_premise, small_tale_dogs_hypothesis, small_tale_dogs_hypothesis))
# ```
# END_EXAMPLE
#
# START_EXAMPLE
# Premise: The 3 performers wore outfits inspired by the Spanish culture.
# Hypothesis: The outfits of the 3 performers were in the colors of Spain's flag.
# Answer:
# ```python
# performers_premise = 3
# performers_hypothesis = 3
#
# def entailment_or_neutral(performers_premise, performers_hypothesis):
#     # the hypothesis mentions a number of performers and their outfits, which are also referenced in the premise
#     # however, outfits being inspired by the spanish culture does not necessarily mean they were in the colors of the Spanish flag
#     # as the extra details in the hypothesis cannot be entailed from the premise, the hypothesis is neutral to the premise
#     return None
#
# print(entailment_or_neutral(performers_premise, performers_hypothesis))
# ```
# END_EXAMPLE
#
# START_EXAMPLE
# Premise: Amsterdam, as the leading city in terms of sustainability projects, allocates $2M to green energy initiatives.
# Hypothesis: Amsterdam's $2M budget for green-energy projects maintains it as a leading city in terms of sustainability projects
# Answer:
# ```python
# budget_premise = 2e6
# budget_hypothesis = 2e6
#
# def entailment_or_neutral(budget_premise, budget_hypothesis):
#     # both the hypothesis and premise mention Amsterdam's budget for green energy, but the hypothesis suggests Amsterdam was already the leading city in terms of sustainability, which is not clear from the premise
#     # as the hypothesis gives details that cannot be fully entailed from the premise, it is neutral to it
#     return None
#
# print(entailment_or_neutral(budget_premise, budget_hypothesis))
# ```
# END_EXAMPLE
# """
#
# rtequant_examples = """START_EXAMPLE
# Premise: There have been more than 10 storms during the past year.
# Hypothesis: Over the last year, more than 10 snowstorms have been reported.
# Answer:
# ```python
# min_storms_premise = 10
# min_snowstorms_hypothesis = 10
#
# def entailment_or_neutral(min_storms_premise, min_snowstorms_hypothesis):
#     # the hypothesis talks about snowstorms which are not referenced in the premise (the type of storm is not mentioned).
#     # The hypothesis cannot be entailed from the premise, since the number of snowstorms is unknown.
#     return None
#
# print(entailment_or_neutral(min_storms_premise, min_snowstorms_hypothesis))
# ```
# END_EXAMPLE
#
# START_EXAMPLE
# Premise: Katty Ruth is the author of 5 personal development books, two of which she released before the age of 30.
# Hypothesis: Katty Ruth released 2 books on personal development before she turned 30.
# Answer:
# ```python
# total_books_premise = 5
# books_before_30_premise = 2
# books_before_30_hypothesis = 2
#
# def entailment_or_neutral(total_books_premise, books_before_30_premise, books_before_30_hypothesis):
#     # the hypothesis talks about the number of books written by Kathy before 30, which are also mentioned in the premise
#     # check if the number of books she wrote before 30 in the hypothesis entails the one in the premise, by checking if they are equal
#     if books_before_30_hypothesis == books_before_30_premise:
#         return True
#     else:
#         return None
#
# print(entailment_or_neutral(total_books_premise, books_before_30_premise, books_before_30_hypothesis))
# ```
# END_EXAMPLE
# """
#
# redditnli_examples = """START_EXAMPLE
# Premise: Two weeks after the controversial study, a report by the ECB asserts that "cryptocurrency poses minimal risk" despite previous warnings.
# Hypothesis: The ECB asserts that "risk is negligible in the crypto market" 2 weeks after a controversial study was published.
# Answer:
# ```python
# weeks_premise = 2
# weeks_hypothesis = 2
#
# def entailment_or_contradiction_or_neutral(weeks_premise, weeks_hypothesis):
#     # the hypothesis and premise mention the number of weeks between a controversial study and the response of the ECB
#     # check if the hypothesis entails the premise by checking if the number of weeks is equal in the two sentences
#     if weeks_premise == weeks_hypothesis:
#         return True
#     else:
#         return False
#
# print(entailment_or_contradiction_or_neutral(weeks_premise, weeks_hypothesis))
# ```
# END_EXAMPLE
#
# START_EXAMPLE
# Premise: 1 out of 100 investors says that they are hopeful the inflation levels will drop
# Hypothesis: American investors are hopeful that inflation will drop in a ratio of 1 to 100.
# Answer:
# ```python
# ratio_premise = 1/100
# ratio_hypothesis = 1/100
#
# def entailment_or_contradiction_or_neutral(ratio_premise, ratio_hypothesis):
#     # the hypothesis and premise mention the ratio of investors hopeful that inflation will decrease
#     # however, the hypothesis links the ratio to american investors, which cannot be entialed from the premise
#     return None
#
# print(entailment_or_contradiction_or_neutral(ratio_premise, ratio_hypothesis))
# ```
# END_EXAMPLE
#
# START_EXAMPLE
# Premise: The top 5 companies in S&P500 make up in earnings more than 60% of the total valuation of start-ups in the US.
# Hypothesis: The top 5 companies in S&P500 make up in earnings more than 70% of the total valuation of start-ups in the US.
# Answer:
# ```python
# number_companies_premise = 5
# min_percentage_of_valuation_premise = 60
# number_companies_hypothesis = 5
# min_percentage_of_valuation_hypothesis = 70
#
# def entailment_or_contradiction_or_neutral(number_companies_premise, min_percentage_of_valuation_premise, number_companies_hypothesis, min_percentage_of_valuation_hypothesis):
#     # the hypothesis and premise mention a selection of companies from S&P500 and how much of the total US start-up value they represent
#     # check if the hypothesis contradicts the premise by checking if the number of companies is not equal between the two sentences
#     if number_companies_premise != number_companies_hypothesis:
#         return False
#     # check if the hypothesised percentage contradicts the premise one by being lower or equal to it
#     if min_percentage_of_valuation_hypothesis <= min_percentage_of_valuation_premise:
#         return False
#     # any percentage higher than 60 will entail the percentage in the premise, so the hypothesis is neutral to the premise, since it does not contradict it and it also does not exclusively entail it
#     return None
#
# print(entailment_or_contradiction_or_neutral(number_companies_premise, min_percentage_of_valuation_premise, number_companies_hypothesis, min_percentage_of_valuation_hypothesis))
# ```
# END_EXAMPLE
# """
#
# stresstest_examples = """START_EXAMPLE
# Premise: He sold $200-worth of cookies at the school fair.
# Hypothesis: He sold cookies worth at least $100.
# Answer:
# ```python
# cookie_sales_premise = 200
# min_cookie_sales_hypothesis = 100
#
# def entailment_or_contradiction_or_neutral(cookie_sales_premise, min_cookie_sales_hypothesis):
#     # the hypothesis refers to the number of sold cookies mentioned in the premise
#     # the hypothesis estimates the cookie sales to more or equal to 'min_cookie_sales_hypothesis'
#     # check if the hypothesis contradicts the premise by checking if cookie sales reported in the premise are lower than 'min_cookie_sales_hypothesis'
#     if cookie_sales_premise < min_cookie_sales_hypothesis:
#         return False
#     else:
#         return True
#
# print(entailment_or_contradiction_or_neutral(cookie_sales_premise, min_cookie_sales_hypothesis))
# ```
# END_EXAMPLE
#
# START_EXAMPLE
# Premise: There are more than 10 roses in the vase.
# Hypothesis: There are 15 roses in the vase.
# Answer:
# ```python
# min_roses_vase_premise = 10
# roses_vase_hypothesis = 15
#
# def entailment_or_contradiction_or_neutral(min_roses_vase_premise, roses_vase_hypothesis):
#     # the hypothesis talks about the number of roses in a vase, referenced also in the premise
#     # check if the hypothesis contradicts the premise estimate of more than 'min_roses_vase_premise', by checking if the number of roses from the hypothesis is lower or equal to 'min_roses_vase_premise'
#     if roses_vase_hypothesis <= min_roses_vase_premise:
#         return False
#     # any number of roses greater than 10 is consistent with the premise, so the hypothesis is neutral to the premise
#     return None
#
# print(entailment_or_contradiction_or_neutral(min_roses_vase_premise, roses_vase_hypothesis))
# ```
# END_EXAMPLE
# """
#
# awpnli_examples = """START_EXAMPLE
# Premise: Yesterday I learned 35 verbs and 5 nouns in the morning and 10 verbs in the evening.
# Hypothesis: I learned 5 nouns and less than fifty verbs yesterday.
# Answer:
# ```python
# verbs_morning_premise = 35
# verbs_evening_premise = 10
# nouns_premise = 5
# max_verbs_hypothesis = 50
# nouns_hypothesis = 5
#
# def entailment_or_contradiction(verbs_morning_premise, verbs_evening_premise, nouns_premise, max_verbs_hypothesis, nouns_hypothesis):
#     # the hypothesis talks about the number of learned nouns and verbs, which are also referenced in the premise
#     # find the total number of verbs learned from the premise
#     total_verbs_premise = verbs_morning_premise + verbs_evening_premise
#     # check if the total verbs form the hypothesis is more than 'verbs_evening_premise' and if the number of nouns is equal between the premise and hypothesis
#     return max_verbs_hypothesis > total_verbs_premise and nouns_premise == nouns_hypothesis
#
# print(entailment_or_contradiction(verbs_morning_premise, verbs_evening_premise, nouns_premise, max_verbs_hypothesis, nouns_hypothesis))
# ```
# END_EXAMPLE
#
# START_EXAMPLE
# Premise: She bought 10 crayons and received 5 more from her desk mate.
# Hypothesis: She has 10 crayons in total.
# Answer:
# ```python
# bought_crayons_premise = 10
# received_crayons_premise = 5
# total_crayons_hypothesis = 12
#
# def entailment_or_contradiction(bought_crayons_premise, received_crayons_premise, total_crayons_hypothesis):
#     # the entity in the hypothesis can be computed from the entities in the premise
#     total_crayons_premise = bought_crayons_premise + received_crayons_premise
#     # check if 'total_crayons_hypothesis' entails the quantity deduced from the premise, so if they are equal
#     return total_crayons_premise == total_crayons_hypothesis:
#
# print(entailment_or_contradiction(bought_crayons_premise, received_crayons_premise, total_crayons_hypothesis))
# ```
# END_EXAMPLE
# """

########################
# template_ecn = """
# You must write Python code starting from 2 input sentences, based on these rules:
# - first you define variables with representative names for the numerical entities in both inputs (one variable per entity, per sentence);
# - extract all quantities as valid numbers (integers or floats). do not ignore any quantity or numerical information;
# - next, use brief comments to explain what comparison you do between the defined variables (do not use their values in the comments). Any comparison you do should be do through code as well.;
# - refrain from concluding in the comments the entailment/contradiction or neutral relation;
# - use the variables to perform calculations if necessary and finally compare them accordingly to infer one of the following:
#     - "entailment", if the hypothesis entails the premise
#     - "contradiction" if the hypothesis contradicts the premise
#     - "neutral" if the hypothesis is neutral to the premise;
# - use the correct comparison operators (i.e., if we know "A is more than B", then we can either check if A>B for entailment or if B<=A for contradiction).
# - sometimes the textual information indicates neutrality and no comparison is needed.
#
# Only answer with the script. To illustrate, consider the following examples:
#
# {examples}
#
# Your turn now:
# Possible labels: entailment, contradiction, neutral
# Premise: {premise}
# Hypothesis: {hypothesis}
# Answer:
# """

template = """
You must write Python code starting from 2 input sentences, based on these rules:
- first you define variables with representative names for the numerical entities in both inputs (one variable per entity, per sentence);
- extract all quantities as valid numbers (integers or floats). do not ignore any quantity or numerical information;
- next, use brief comments to explain what comparison you do between the defined variables (do not use their values in the comments). Any comparison you do should be do through code as well.;
- refrain from concluding in the comments the entailment/contradiction or neutral relation;
- use the variables to perform calculations if necessary and finally compare them accordingly to infer one of the following: 
{script_output_options}
- use the correct comparison operators (i.e., if we know "A is more than B", then we can either check if A>B for entailment or if B<=A for contradiction).
- sometimes the textual information indicates neutrality and no comparison is needed.

Only answer with the script. To illustrate, consider the following examples:

{examples}

Your turn now:
Possible labels: {labels}
Premise: {premise}
Hypothesis: {hypothesis}
Answer:
"""

ecn_options = """    
    - "entailment": the hypothesis can be fully and explicitly entailed from the premise
    - "contradiction": at least one aspect in the hypothesis contradicts the premise
    - "neutral": the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
"""

ecn_labels = "entailment, contradiction, neutral"

ec_options = """    
    - "entailment": the hypothesis can be fully and explicitly entailed from the premise
    - "contradiction": at least one aspect in the hypothesis contradicts the premise
"""

ec_labels = "entailment, contradiction"

en_options = """    
    - "entailment": the hypothesis can be fully and explicitly entailed from the premise
    - "neutral": the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
"""

en_labels = ecn_labels


# stresstest_examples = """
# START_EXAMPLE
# Possible labels: entailment, contradiction, neutral
# Premise: He sold $200-worth of cookies at the school fair and 15 pies.
# Hypothesis: He sold cookies worth more than $100 and 15 pies.
# Answer:```python
# cookie_sales_premise = 200
# min_cookie_sales_hypothesis = 100
# pies_sold_premise = 15
# pies_sold_hypothesis = 15
#
# # the hypothesis refers to the number of sold cookies and pies mentioned in the premise
# # the hypothesis estimates the cookie sales to more than 'min_cookie_sales_hypothesis'
# # check if the hypothesis contradicts the premise by checking if cookie sales reported in the premise are lower or equal to 'min_cookie_sales_hypothesis' or if the number of pies reported in the hypothesis is not equal to 'pies_sold_premise'
# if cookie_sales_premise <= min_cookie_sales_hypothesis or pies_sold_premise != pies_sold_hypothesis:
#     label = "contradiction"
# else:
#     label = "entailment"
#
# print(label)
# ```
# END_EXAMPLE
#
# START_EXAMPLE
# Possible labels: entailment, contradiction, neutral
# Premise: There are more than 10 roses in the vase.
# Hypothesis: There are 15 roses in the vase.
# Answer:```python
# min_roses_vase_premise = 10
# roses_vase_hypothesis = 15
#
# # the hypothesis talks about the number of roses in a vase, referenced also in the premise
# # check if the hypothesis contradicts the premise estimate of more than 'min_roses_vase_premise', by checking if the number of roses from the hypothesis is lower or equal to 'min_roses_vase_premise'
# if roses_vase_hypothesis <= min_roses_vase_premise:
#     label = "contradiction"
# # any number of roses greater than 'min_roses_vase_premise' is consistent with the premise, so the hypothesis is neutral to the premise
# label = "neutral"
#
# print(label)
# ```
# END_EXAMPLE
# """

stresstest_examples = """START_EXAMPLE
Possible labels: entailment, contradiction, neutral
Premise: He sold $200-worth of cookies at the school fair and 15 pies.
Hypothesis: He sold cookies worth more than $100 and 15 pies.
Answer:```python
cookie_sales_premise = 200
cookie_sales_hypothesis = 100
pies_sold_premise = 15
pies_sold_hypothesis = 15

# the hypothesis refers to the number of sold cookies and pies mentioned in the premise
if cookie_sales_premise <= cookie_sales_hypothesis:
    # check if the estimate of 'cookie_sales_hypothesis' contradicts the number of cookie sales in the premise
    label = "contradiction"
elif pies_sold_hypothesis != pies_sold_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
```
END_EXAMPLE

START_EXAMPLE
Possible labels: entailment, contradiction, neutral
Premise: There are more than 10 roses in the vase.
Hypothesis: There are 15 roses in the vase.
Answer:```python
roses_vase_premise = 10
roses_vase_hypothesis = 15

# the hypothesis talks about the number of roses in a vase, referenced also in the premise
if roses_vase_hypothesis <= roses_vase_premise:
    # check if the hypothesis value contradicts the estimate of more than 'roses_vase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
```
END_EXAMPLE"""

awpnli_examples = """START_EXAMPLE
Possible labels: entailment, contradiction
Premise: Yesterday I learned 35 verbs and 5 nouns in the morning and 10 verbs in the evening.
Hypothesis: I learned 5 nouns and less than fifty verbs yesterday.
Answer:```python
verbs_morning_premise = 35
verbs_evening_premise = 10
verbs_hypothesis = 50 
nouns_premise = 5
nouns_hypothesis = 5

# the hypothesis talks about the number of learned nouns and verbs, which are also referenced in the premise
# find the total number of verbs learned from the premise 
total_verbs_premise = verbs_morning_premise + verbs_evening_premise
if max_verbs_hypothesis >= total_verbs_premise:
    # check if the total verbs from the hypothesis contradict the estimate of more than 'verbs_evening_premise'
    label = "contradiction"
elif nouns_hypothesis != nouns_premise:
    # check if the number of nouns from the hypothesis contradicts the number of nouns in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
```
END_EXAMPLE

START_EXAMPLE
Possible labels: entailment, contradiction
Premise: She bought 10 crayons and received 5 more from her desk mate.
Hypothesis: She has 10 crayons in total.
Answer:```python
bought_crayons_premise = 10
received_crayons_premise = 5
total_crayons_hypothesis = 12

# the hypothesis refers to the number of crayons, which are also mentioned in the premise
# compute the total number of crayons in the premise
total_crayons_premise = bought_crayons_premise + received_crayons_premise
if total_crayons_hypothesis != total_crayons_premise:
    # check if the number of crayons in the hypothesis contradicts the number of crayons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
```
END_EXAMPLE"""

newsnli_examples = """START_EXAMPLE
Possible labels: entailment, contradiction, neutral
Premise: Nationwide beach cleanup effort attracts 10,000 volunteers.
Hypothesis: Ten thousand volunteers join the second round of the beach cleanup effort nationwide.
Answer:```python
volunteers_premise = 10000
volunteers_hypothesis = 10000

# the hypothesis mentions the number of nationwide volunteers for beach cleanup, which is also referenced in the premise
# however, the hypothesis refers to the second phase of this initiative, which cannot be entailed from the premise
label = "neutral"

print(label)
```
END_EXAMPLE

START_EXAMPLE
Possible labels: entailment, contradiction, neutral
Premise: Economic boom: U.S. GDP grows 4.5% in first quarter, surpassing expectations with a 2 million job increase.
Hypothesis: First quarter U.S. economic growth hits 4.5%, exceeding forecasts and adding 2 million new jobs.
Answer:```python
gdp_growth_premise = 0.045
gdp_growth_hypothesis = 0.045
new_jobs_premise = 2000000
new_jobs_hypothesis = 2000000

# the hypothesis mentions the GDP growth and the job increase in the U.S., which are also mentioned in the premise
if gdp_growth_hypothesis != gdp_growth_premise:
    # check if the gdp growth in the hypothesis contradicts the gdp growth reported in the premise
    label = "contradiction"
elif new_jobs_hypothesis != new_jobs_premise:
    # check if the number of new jobs from the hypothesis contradicts the number of new jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
```
END_EXAMPLE"""

rtequant_examples = """START_EXAMPLE
Possible labels: entailment, contradiction, neutral
Premise: There have been more than 10 million cases of flu during the past year.
Hypothesis: Over the last year, more than 10 million cases of type A flu have been reported.
Answer:```python
flu_cases_premise = 10e6
flu_cases_hypothesis = 10e6

# the hypothesis talks about the number of type A flu cases which are not referenced in the premise (the type of flu is not mentioned)
# the hypothesis cannot be entailed from the premise, since the number of type A flu cases is unknown.
label = "neutral"

print(label)
```
END_EXAMPLE

START_EXAMPLE
Possible labels: entailment, contradiction, neutral
Premise: Katty Ruth is the author of 5 personal development books, two of which she released before the age of 30.
Hypothesis: Katty Ruth released 2 books on personal development before she turned 30.
Answer:```python
total_books_premise = 5
books_before_age_premise = 2
books_before_age_hypothesis = 2
age_premise = 30
age_hypothesis = 30

# the hypothesis talks about the number of books written by Kathy before a certain age, which is also mentioned in the premise
if books_before_age_hypothesis != books_before_age_premise:
    # check if the number of books written before the given age in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
elif age_hypothesis != age_premise:
    # check if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
```
END_EXAMPLE"""

redditnli_examples = """START_EXAMPLE
Possible labels: entailment, contradiction, neutral
Premise: Two weeks after the controversial study, a report by the ECB asserts that "cryptocurrency poses minimal risk" despite previous warnings.
Hypothesis: The ECB asserts that "risk is negligible in the crypto market" 2 weeks after a controversial study was published.
Answer:```python
weeks_premise = 2
weeks_hypothesis = 2

# the hypothesis and premise mention the number of weeks between a controversial study and the response of the ECB
if weeks_hypothesis != weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the number of weeks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
```
END_EXAMPLE

START_EXAMPLE
Possible labels: entailment, contradiction, neutral
Premise: 6 out of 100 investors says that they are hopeful the inflation levels will drop.
Hypothesis: 6% of American investors are hopeful that inflation will decrease.
Answer:```python
ratio_premise = 6/100
ratio_hypothesis = 0.06

# the hypothesis and premise mention the ratio of investors hopeful that inflation will decrease
# however, the hypothesis links the ratio to american investors, which cannot be entitles from the premise
label = "neutral"

print(label)
```
END_EXAMPLE

START_EXAMPLE
Possible labels: entailment, contradiction, neutral
Premise: The top 5 companies in S&P500 make up in earnings more than 60% of the total valuation of start-ups in the US.
Hypothesis: The top 5 companies in S&P500 make up in earnings more than 70% of the total valuation of start-ups in the US.
Answer:```python
number_companies_premise = 5
number_companies_hypothesis = 5
percentage_of_valuation_premise = 60
percentage_of_valuation_hypothesis = 70

# the hypothesis and premise mention a selection of companies from S&P500 and how much of the total US start-up value they represent
if number_companies_premise != number_companies_hypothesis:
    # check if the number of companies in the hypothesis contradicts the number of companies in the premise
    label = "contradiction"
elif percentage_of_valuation_hypothesis < min_percentage_of_valuation_premise:
    # check if the estimated percentage of the total valuation in the hypothesis contradicts the premise estimate of more than 'percentage_of_valuation_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the valuation
    # any estimate of the percentage in the hypothesis greater or equal to 'percentage_of_valuation_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
```
END_EXAMPLE"""
########################


def get_prompt(prompt_type: str) -> PromptTemplate:
    """Returns a Langchain prompt with imputed few-shot examples, based on the selected dataset"""
    if prompt_type == "redditnli":
        # return PromptTemplate.from_template(template_ecn.replace("{examples}", redditnli_examples))
        return PromptTemplate.from_template(template.replace("{examples}", redditnli_examples).replace("{script_output_options}", ecn_options).replace("{labels}", ecn_labels))
    elif prompt_type == "newsnli":
        # return PromptTemplate.from_template(template_en.replace("{examples}", newsnli_examples))
        return PromptTemplate.from_template(template.replace("{examples}", newsnli_examples).replace("{script_output_options}", en_options).replace("{labels}", en_labels))
    elif prompt_type == "rtequant":
        # return PromptTemplate.from_template(template_en.replace("{examples}", rtequant_examples))
        return PromptTemplate.from_template(template.replace("{examples}", rtequant_examples).replace("{script_output_options}", en_options).replace("{labels}", en_labels))
    elif prompt_type == "awpnli":
        # return PromptTemplate.from_template(template_ec.replace("{examples}", awpnli_examples))
        return PromptTemplate.from_template(template.replace("{examples}", awpnli_examples).replace("{script_output_options}", ec_options).replace("{labels}", ec_labels))
    elif prompt_type == "stresstest":
        # return PromptTemplate.from_template(template_ecn.replace("{examples}", stresstest_examples))
        return PromptTemplate.from_template(template.replace("{examples}", stresstest_examples).replace("{script_output_options}", ecn_options).replace("{labels}", ecn_labels))


# def format_prompt(prompt_type: str, input_sample: dict) -> Optional[str | None]:
#     """
#     Prepares a prompt for a specified dataset and imputes inputs from a given sample (premise and hypothesis).
#     Add `### Instruction:` and `### Input:` markers, in line with the instruction-tuning prompt format for fine-tuning.
#     :param prompt_type: the prompt type, the dataset name in lowercase, with removed non-letter chars
#     :param input_sample: a dict representing a sample with a premise and a hypothesis
#     :return: a formatted prompt
#     """
#     if prompt_type == "redditnli":
#         template = template_ecn.replace("\n", "").replace("Answer:", "").replace("{examples}", redditnli_examples)
#     elif prompt_type == "newsnli":
#         template = template_en.replace("\n", "").replace("Answer:", "").replace("{examples}", newsnli_examples)
#     elif prompt_type == "rtequant":
#         template = template_en.replace("\n", "").replace("Answer:", "").replace("{examples}", rtequant_examples)
#     elif prompt_type == "awpnli":
#         template = template_ec.replace("\n", "").replace("Answer:", "").replace("{examples}", awpnli_examples)
#     elif prompt_type == "stresstest":
#         template = template_ecn.replace("\n", "").replace("Answer:", "").replace("{examples}", stresstest_examples)
#     else:
#         return None
#     template_with_vars = template.replace("{premise}", f'{input_sample["premise"]}'). \
#         replace("{hypothesis}", input_sample["hypothesis"])
#     template_with_vars = template_with_vars.replace("Your turn now:", "### Input:\n")
#     return f"### Instruction:\n{template_with_vars}".strip()


# def format_prompt(prompt_type: str, input_sample: dict) -> Optional[str | None]:
#     """
#     Prepares a prompt for a specified dataset and imputes inputs from a given sample (premise and hypothesis).
#     Add `### Instruction:` and `### Input:` markers, in line with the instruction-tuning prompt format for fine-tuning.
#     :param prompt_type: the prompt type, the dataset name in lowercase, with removed non-letter chars
#     :param input_sample: a dict representing a sample with a premise and a hypothesis
#     :return: a formatted prompt
#     """
#     if prompt_type == "redditnli":
#         template = template_ecn.replace("\n", "").replace("Answer:", "").replace("{examples}", redditnli_examples)
#     elif prompt_type == "newsnli":
#         template = template_en.replace("\n", "").replace("Answer:", "").replace("{examples}", newsnli_examples)
#     elif prompt_type == "rtequant":
#         template = template_en.replace("\n", "").replace("Answer:", "").replace("{examples}", rtequant_examples)
#     elif prompt_type == "awpnli":
#         template = template_ec.replace("\n", "").replace("Answer:", "").replace("{examples}", awpnli_examples)
#     elif prompt_type == "stresstest":
#         template = template_ecn.replace("\n", "").replace("Answer:", "").replace("{examples}", stresstest_examples)
#     else:
#         return None
#     template_with_vars = template.replace("{premise}", f'{input_sample["premise"]}'). \
#         replace("{hypothesis}", input_sample["hypothesis"])
#     template_with_vars = template_with_vars.replace("Your turn now:", "### Input:\n")
#     return f"### Instruction:\n{template_with_vars}".strip()


# template for the scrips which will be saved in .py files, for manual annotator validation
python_script_template = """# Premise: {premise}
# Hypothesis: {hypothesis}
# Golden Label: {label}

{script}
"""


if __name__ == "__main__":
    print(format_prompt("stresstest", {"premise": "some premise", "hypothesis": "some hypothesis"}))
