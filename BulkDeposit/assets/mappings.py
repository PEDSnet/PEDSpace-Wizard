METADATA_TO_DUBLIN_XML_MAPPING = {
    "Title": {"element": "title", "qualifier": "none"},
    "Creator_01": {"element": "contributor", "qualifier": "other"},
    "Date_Created": {"element": "date", "qualifier": "created"},
    "Reviewer_01": {"element": "contributor", "qualifier": "advisor"},
    "Affiliation_01": {"element": "contributor", "qualifier": "other"},
    "Intention": {"element": "description", "qualifier": "abstract"},
    "Vocabulary_01": {"element": "subject", "qualifier": "other"},
    "Vocabulary_02": {"element": "subject", "qualifier": "other"},
    "Vocabulary_03": {"element": "subject", "qualifier": "other"},
    "Vocabulary_04": {"element": "subject", "qualifier": "other"},
    "Vocabulary_05": {"element": "subject", "qualifier": "other"},
    "Tags_01": {"element": "subject", "qualifier": "none"},
    "Tags_02": {"element": "subject", "qualifier": "none"},
    "Tags_03": {"element": "subject", "qualifier": "none"},
    "Tags_04": {"element": "subject", "qualifier": "none"},
    "Tags_05": {"element": "subject", "qualifier": "none"},
    "Description": {"element": "description", "qualifier": "none"},
    "Provenance": {"element": "description", "qualifier": "provenance"},
    "Dev_Code": {"element": "relation", "qualifier": "uri"},
    "MeSH_01": {"element": "subject", "qualifier": "mesh"},
    "MeSH_02": {"element": "subject", "qualifier": "mesh"},
    "MeSH_03": {"element": "subject", "qualifier": "mesh"},
    "MeSH_04": {"element": "subject", "qualifier": "mesh"},
    "MeSH_05": {"element": "subject", "qualifier": "mesh"},
    "Publisher": {"element": "publisher", "qualifier": "none"},
    "Rights_Statement": {"element": "rights", "qualifier": "none"},
    "License": {"element": "rights", "qualifier": "uri"}
}

DOMAIN_TO_THUMBNAIL_FILE_MAPPING = {
   "Device": "DEVICES.png",
   "Diagnoses": "DIAGNOSES.png",
   "Environmental and Socioeconomic Variables": "AREA-LEVEL.png",
   "Lab Results": "LAB RESULTS.png",
   "Medications": "MEDICATIONS.png",
   "Physiological Measurements": "PHYSMEAS.png",
   "Procedures": "PROCEDURES.png",
   "Visits": "VISITS.png"
}

DOMAIN_TO_COLLECTION_MAPPING ={
   "Device": "20.500.14642/13",
   "Diagnoses": "20.500.14642/14",
   "Environmental and Socioeconomic Variables": "20.500.14642/12",
   "Lab Results": "20.500.14642/15",
   "Medications": "20.500.14642/16",
   "Physiological Measurements": "20.500.14642/17",
   "Procedures": "20.500.14642/18",
   "Visits": "20.500.14642/19"
}
