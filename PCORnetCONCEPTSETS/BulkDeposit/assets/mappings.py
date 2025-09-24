METADATA_TO_DUBLIN_XML_MAPPING = {
    "Title": {"element": "title", "qualifier": "none"},

    "Date_Created": {"element": "date", "qualifier": "created"},

    "Creator_01": {"element": "contributor", "qualifier": "author"},
    "Creator_02": {"element": "contributor", "qualifier": "author"},
    "Creator_02": {"element": "contributor", "qualifier": "author"},

    "Evaluation_Level": {"element": "subject", "qualifier": "none"},

    "Reviewer_01": {"element": "contributor", "qualifier": "advisor"},
    "Reviewer_02": {"element": "contributor", "qualifier": "advisor"},
    "Reviewer_03": {"element": "contributor", "qualifier": "advisor"},

    "Affiliation_01": {"element": "contributor", "qualifier": "other"},
    "Affiliation_02": {"element": "contributor", "qualifier": "other"},
    "Affiliation_03": {"element": "contributor", "qualifier": "other"},

    "Intention": {"element": "description", "qualifier": "abstract"},

    "Vocabulary_01": {"element": "subject", "qualifier": "other"},
    "Vocabulary_02": {"element": "subject", "qualifier": "other"},
    "Vocabulary_03": {"element": "subject", "qualifier": "other"},
    "Vocabulary_04": {"element": "subject", "qualifier": "other"},
    "Vocabulary_05": {"element": "subject", "qualifier": "other"},
    "Vocabulary_06": {"element": "subject", "qualifier": "other"},
    "Vocabulary_07": {"element": "subject", "qualifier": "other"},
    "Vocabulary_08": {"element": "subject", "qualifier": "other"},

    "Tags_01": {"element": "subject", "qualifier": "none"},
    "Tags_02": {"element": "subject", "qualifier": "none"},
    "Tags_03": {"element": "subject", "qualifier": "none"},
    "Tags_04": {"element": "subject", "qualifier": "none"},
    "Tags_05": {"element": "subject", "qualifier": "none"},

    "Description": {"element": "description", "qualifier": "none"},
    "Provenance": {"element": "provenance", "qualifier": "none"},
    "Dev_Code": {"element": "relation", "qualifier": "uri"},

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
## METADATA_TO_LOCAL_XML_MAPPING = {
##    }

METADATA_TO_DSPACE_XML_MAPPING = {
    "Type": {"element": "entity", "qualifier": "type"}
}

## DOMAIN_TO_THUMBNAIL_FILE_MAPPING = {
##   "Device": "DEVICES.png",
##   "Diagnoses": "DIAGNOSES.png",
##   "Environmental and Socioeconomic Variables": "AREA-LEVEL.png",
##   "Lab Results": "LAB RESULTS.png",
##   "Medications": "MEDICATIONS.png",
##   "Physiological Measurements": "PHYSMEAS.png",
##   "Procedures": "PROCEDURES.png",
##   "Visits": "VISITS.png"
##}

DOMAIN_TO_COLLECTION_MAPPING ={
   "Environmental and Socioeconomic Variables": "123456789/32",
   "Device": "123456789/31",
   "Diagnoses": "123456789/6",
   "Lab Results": "123456789/19",
   "Medications": "123456789/15",
   "Physiological Measurements": "123456789/18",
   "Procedures": "123456789/4",
   "Visits": "123456789/33"
}
