from pytrials.client import ClinicalTrials
import pandas as pd


'''
get_study_fields: fields
NCTID = Trial ID
Study Title
Phase = Phase 1/2/3/4
Condition = Disease/condition
InterventionName = Drug/treatment name
PrimaryOutcomeMeasure = Primary endpoint
EnrollmentCount = Number of participants
OverallStatus = Recruiting, compilcated, etc.
ComplettionDate = Estimated/actual completion
Sponsor = Lead Sponsor
'''

ct = ClinicalTrials()

# max_studies limit is 1000

results = ct.get_full_studies(search_expr="endometriosis", max_studies = 50)
#print(results)

fields = ct.get_study_fields(
    search_expr="endometriosis",
    fields = ["NCT Number", "Study Title", "Conditions", "Phases", "Interventions", 
              "Primary Outcome Measures", "Enrollment", "Study Status", "Completion Date", "Sponsor"
              ,"Sex", "Age", "Funder Type", "Study Type"],
    max_studies = 1000,
    fmt = "csv"
)

endo_df = pd.DataFrame.from_records(fields[1:], columns = fields[0])
print(endo_df)

