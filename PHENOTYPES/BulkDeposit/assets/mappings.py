METADATA_TO_DUBLIN_XML_MAPPING = {
    "Title": {"element": "title", "qualifier": "none"},
    "Date_Created": {"element": "date", "qualifier": "created"},

    "Creator_01": {"element": "contributor", "qualifier": "author"},
    "Creator_02": {"element": "contributor", "qualifier": "author"},
    "Creator_03": {"element": "contributor", "qualifier": "author"},
    
    "Affiliation_01": {"element": "contributor", "qualifier": "other"},
    "Affiliation_02": {"element": "contributor", "qualifier": "other"},
    "Affiliation_03": {"element": "contributor", "qualifier": "other"},

    "Phenotype_Description": {"element": "description", "qualifier": "abstract"},
    "Algorithm_Description": {"element": "description", "qualifier": "none"},

    "Algorithm_Component_01": {"element": "subject", "qualifier": "other"},
    "Algorithm_Component_02": {"element": "subject", "qualifier": "other"},
    "Algorithm_Component_03": {"element": "subject", "qualifier": "other"},
    "Algorithm_Component_04": {"element": "subject", "qualifier": "other"},
    "Algorithm_Component_05": {"element": "subject", "qualifier": "other"},
    
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
    "Data_Model": {"element": "subject", "qualifier": "DataModel"},
    "Database_Version": {"element": "admin", "qualifier": "note"},
    "Dev_Strategy_01": {"element": "subject", "qualifier": "flat"},
    "Dev_Strategy_02": {"element": "subject", "qualifier": "flat"},
    "Dev_Strategy_03": {"element": "subject", "qualifier": "flat"},
    "Dev_Strategy_04": {"element": "subject", "qualifier": "flat"},
    "Dev_Population_Age": {"element": "subject", "qualifier": "DevPop"},
    "Dev_Population_Gender": {"element": "subject", "qualifier": "DevPop"},
    "Dev_Population_Race": {"element": "subject", "qualifier": "DevPop"},
    "Validation": {"element": "subject", "qualifier": "validation"},
    "Research_Suitability": {"element": "quality", "qualifier": "status"}
}

METADATA_TO_DSPACE_XML_MAPPING = {
    "Type": {"element": "entity", "qualifier": "type"}
}

DOMAIN_TO_THUMBNAIL_FILE_MAPPING = {
   "Cardiovascular Phenotypes": "PHENOTYPE.png",
   "Congenital, Hereditary, and Neonatal Disease and Abnormality Phenotypes": "PHENOTYPE.png",
   "Digestive System Phenotypes": "PHENOTYPE.png",
   "Endocrine System Phenotypes": "PHENOTYPE.png",
   "Eye Condition Phenotypes": "PHENOTYPE.png",
   "Hemic and Lymphatic Phenotypes": "PHENOTYPE.png",
   "Immune System Phenotypes": "PHENOTYPE.png",
   "Infection Phenotypes": "PHENOTYPE.png",
   "Musculoskeletal Phenotypes": "PHENOTYPE.png",
   "Neoplasm Phenotypes": "PHENOTYPE.png",
   "Nervous System Phenotypes": "PHENOTYPE.png",
   "Nutritional and Metabolic Phenotypes": "PHENOTYPE.png",
   "Otorhinolaryngologic Phenotypes": "PHENOTYPE.png",
   "Pathological Conditions, Signs and Symptoms": "PHENOTYPE.png",
   "Population Characteristics: Socioeconomic and Environmental Impacts": "PHENOTYPE.png",
   "Psychiatric and Psychological Phenotypes": "PHENOTYPE.png",
   "Respiratory Tract Phenotypes": "PHENOTYPE.png",
   "Skin and Connective Tissue Phenotypes": "PHENOTYPE.png",
   "Stomatognathic Phenotypes": "PHENOTYPE.png",
   "Urogenital Phenotypes": "PHENOTYPE.png"
}

DOMAIN_TO_COLLECTION_MAPPING ={
   "Cardiovascular Phenotypes": "20.500.14642/815",
   "Congenital, Hereditary, and Neonatal Disease and Abnormality Phenotypes": "20.500.14642/811",
   "Digestive System Phenotypes": "20.500.14642/814",
   "Endocrine System Phenotypes": "20.500.14642/812",
   "Eye Condition Phenotypes": "20.500.14642/813",
   "Hemic and Lymphatic Phenotypes": "20.500.14642/1145",
   "Immune System Phenotypes": "20.500.14642/1146",
   "Infection Phenotypes": "20.500.14642/1147",
   "Musculoskeletal Phenotypes": "20.500.14642/1148",
   "Neoplasm Phenotypes": "20.500.14642/1149",
   "Nervous System Phenotypes": "20.500.14642/1150",
   "Nutritional and Metabolic Phenotypes": "20.500.14642/1151",
   "Otorhinolaryngologic Phenotypes": "20.500.14642/1152",
   "Pathological Conditions, Signs and Symptoms": "20.500.14642/1153",
   "Population Characteristics: Socioeconomic and Environmental Impacts": "20.500.14642/1154",
   "Psychiatric and Psychological Phenotypes": "20.500.14642/1155",
   "Respiratory Tract Phenotypes": "20.500.14642/1156",
   "Skin and Connective Tissue Phenotypes": "20.500.14642/817",
   "Stomatognathic Phenotypes": "20.500.14642/816",
   "Urogenital Phenotypes": "20.500.14642/794"
}
