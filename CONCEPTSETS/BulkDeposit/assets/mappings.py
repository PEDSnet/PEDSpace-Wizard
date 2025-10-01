METADATA_TO_DUBLIN_XML_MAPPING = {
    "Title": {"element": "title", "qualifier": "none"},

    "Date_Created": {"element": "date", "qualifier": "created"},

    "Creator_01": {"element": "contributor", "qualifier": "author"},
    "Creator_02": {"element": "contributor", "qualifier": "author"},
    "Creator_02": {"element": "contributor", "qualifier": "author"},

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

METADATA_TO_LOCAL_XML_MAPPING = {
    "Evaluation_Level": {"element": "subject", "qualifier": "EvalType"},
    "Data_Model": {"element": "subject", "qualifier": "DataModel"},
    "Database_Version": {"element": "admin", "qualifier": "note"},
    "Med_Characterization_01": {"element": "subject", "qualifier": "MedTermChar"},
    "Med_Characterization_02": {"element": "subject", "qualifier": "MedTermChar"},
    "Med_Characterization_03": {"element": "subject", "qualifier": "MedTermChar"},
    "Med_Characterization_04": {"element": "subject", "qualifier": "MedTermChar"},
    "Tags_01": {"element": "subject", "qualifier": "flat"},
    "Tags_02": {"element": "subject", "qualifier": "flat"},
    "Tags_03": {"element": "subject", "qualifier": "flat"},
    "Tags_04": {"element": "subject", "qualifier": "flat"},
    "Tags_05": {"element": "subject", "qualifier": "flat"},
    "Research_Suitability": {"element": "quality", "qualifier": "status"}
}

METADATA_TO_DSPACE_XML_MAPPING = {
    "Type": {"element": "entity", "qualifier": "type"}
}

DOMAIN_TO_THUMBNAIL_FILE_MAPPING = {
   "Device": "CONCEPTSET.png",
   "Diagnoses": "CONCEPTSET.png",
   "Environmental and Socioeconomic Variables": "CONCEPTSET.png",
   "Lab Results": "CONCEPTSET.png",
   "Medications": "CONCEPTSET.png",
   "Physiological Measurements": "CONCEPTSET.png",
   "Procedures": "CONCEPTSET.png",
   "Visits": "CONCEPTSET.png"
}

DOMAIN_TO_COLLECTION_MAPPING ={
   "Environmental and Socioeconomic Variables": "20.500.14642/12",
   "Device": "20.500.14642/13",
   "Diagnoses": "20.500.14642/14",
   "Lab Results": "20.500.14642/15",
   "Medications": "20.500.14642/16",
   "Physiological Measurements": "20.500.14642/17",
   "Procedures": "20.500.14642/18",
   "Visits": "20.500.14642/19"
}
