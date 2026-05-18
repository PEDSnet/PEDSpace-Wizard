from tkinter import Variable
from pandas import Categorical

METADATA_TO_DUBLIN_XML_MAPPING = {
    "Title": {"element": "title", "qualifier": "none"},
    "Analysis_Type": {"element": "type", "qualifier": "none"},
    "Date_Created": {"element": "date", "qualifier": "created"},

    "Creator_01": {"element": "contributor", "qualifier": "author"},
    "Creator_02": {"element": "contributor", "qualifier": "author"},
    "Creator_03": {"element": "contributor", "qualifier": "author"},

    "Affiliation_01": {"element": "contributor", "qualifier": "other"},
    "Affiliation_02": {"element": "contributor", "qualifier": "other"},
    "Affiliation_03": {"element": "contributor", "qualifier": "other"},

    "Evaluation_Parameters_01": {"element": "subject", "qualifier": "none"},
    "Evaluation_Parameters_02": {"element": "subject", "qualifier": "none"},
    "Evaluation_Parameters_03": {"element": "subject", "qualifier": "none"},

    "checkdesc": {"element": "description", "qualifier": "abstract"},
    "Result_Description": {"element": "description", "qualifier": "none"},
    "Provenance": {"element": "provenance", "qualifier": "none"},

    "MeSH_01": {"element": "subject", "qualifier": "mesh"},
    "MeSH_02": {"element": "subject", "qualifier": "mesh"},
    "MeSH_03": {"element": "subject", "qualifier": "mesh"},
    "MeSH_04": {"element": "subject", "qualifier": "mesh"},
    "MeSH_05": {"element": "subject", "qualifier": "mesh"},
    "MeSH_06": {"element": "subject", "qualifier": "mesh"},
    "MeSH_07": {"element": "subject", "qualifier": "mesh"},

    "Publisher": {"element": "publisher", "qualifier": "none"},
    "Rights_Statement": {"element": "rights", "qualifier": "none"},
    "License": {"element": "rights", "qualifier": "uri"}
}

METADATA_TO_LOCAL_XML_MAPPING = {
    "Result_Observations_01": {"element": "dqcheck", "qualifier": "resultobs"},
    "Result_Observations_02": {"element": "dqcheck", "qualifier": "resultobs"},
    "Result_Observations_03": {"element": "dqcheck", "qualifier": "resultobs"},
    
    "Outcomes_01": {"element": "dqcheck", "qualifier": "outcomes"},
    "Outcomes_02": {"element": "dqcheck", "qualifier": "outcomes"},

    "Outcomes_Description": {"element": "description", "qualifier": "outcomes"},

    "Data_Provenance": {"element": "subject", "qualifier": "DataModel"},

    "Database_Version": {"element": "admin", "qualifier": "note"},

    "DataSource_01": {"element": "subject", "qualifier": "DataProv"},
    "DataSource_02": {"element": "subject", "qualifier": "DataProv"},
    "DataSource_03": {"element": "subject", "qualifier": "DataProv"},
    "DataSource_04": {"element": "subject", "qualifier": "DataProv"},
    "DataSource_05": {"element": "subject", "qualifier": "DataProv"},
    "DataSource_06": {"element": "subject", "qualifier": "DataProv"}
}

METADATA_TO_DSPACE_XML_MAPPING = {
    "Type": {"element": "entity", "qualifier": "type"}
}

DOMAIN_TO_COLLECTION_MAPPING ={
    "Clinical Data Values and Ranges Data Quality Check": "20.500.14642/1057",
    "Categorical Variable Distributions Data Quality Check": "20.500.14642/1130",
    "Patient Event Sequencing Data Quality Check": "20.500.14642/1059",
    "Patient Facts Data Quality Check": "20.500.14642/1125",
    "Patient Records Consistency Data Quality Check": "20.500.14642/1126",
    "Cohort Attrition Data Quality Check": "20.500.14642/1127",
    "Sensitivity to Selection Criteria Data Quality Check": "20.500.14642/1128",
    "Concept Set Distributions Data Quality Check": "20.500.14642/1129",
    "Source and Concept Vocabularies Data Quality Check": "20.500.14642/1027",
    "Unmapped Concepts Data Quality Check": "20.500.14642/1600",
    "Clinical Metadata Data Quality Check": "20.500.14642/1131",
    "Duplicate Record Check Data Quality Check": "20.500.14642/1132",
    "Unit and Value Alignment Data Quality Check": "20.500.14642/1133",
    "Clinical Events and Specialty Agreements Data Quality Check ": "20.500.14642/1134",
    "Date Sequencing Data Quality Check": "20.500.14642/1135",
    "Visit Clinical Data Agreement Data Quality Check": "20.500.14642/1136",
    "Expected Variables Present Data Quality Check": "20.500.14642/1137",
    "Quantitative Variable Distributions Data Quality Check": "20.500.14642/1138"
}