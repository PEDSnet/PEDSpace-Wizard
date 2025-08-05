METADATA_TO_DUBLIN_XML_MAPPING = {
    "Title": {"element": "title", "qualifier": "none"},
    "Funder": {"element": "contributor", "qualifier": "none"},
    "Creator_01": {"element": "contributor", "qualifier": "author"},
    "Creator_02": {"element": "contributor", "qualifier": "author"},
    "Creator_03": {"element": "contributor", "qualifier": "author"},
    "Affiliation_01": {"element": "contributor", "qualifier": "other"},
    "Affiliation_02": {"element": "contributor", "qualifier": "other"},
    "Affiliation_03": {"element": "contributor", "qualifier": "other"},
    "Date_Created": {"element": "date", "qualifier": "created"},
    "Category": {"element": "subject", "qualifier": "none"},
    "Check_Description": {"element": "description", "qualifier": "abstract"},
    "Check_Access": {"element": "description", "qualifier": "abstract"},
    "Viz_01": {"element": "subject", "qualifier": "none"},
    "Viz_02": {"element": "subject", "qualifier": "none"},
    "Viz_03": {"element": "subject", "qualifier": "none"},
    "Dev_Code": {"element": "relation", "qualifier": "uri"},
    "Publisher": {"element": "publisher", "qualifier": "none"},
    "Rights_Statement": {"element": "rights", "qualifier": "none"},
    "License": {"element": "rights", "qualifier": "uri"},
    "Analysis_Level": {"element": "subject", "qualifier": "none"},
    "Clinical_Probe_01": {"element": "subject", "qualifier": "none"},
    "Clinical_Probe_02": {"element": "subject", "qualifier": "none"},
    "Clinical_Probe_03": {"element": "subject", "qualifier": "none"},
    "DQ_Probe_01": {"element": "subject", "qualifier": "none"},
    "DQ_Probe_01": {"element": "subject", "qualifier": "none"},
    "DQ_Probe_01": {"element": "subject", "qualifier": "none"}
}

METADATA_TO_LOCAL_XML_MAPPING = {
    "RawData_Description": {"element": "description", "qualifier": "raw"},
    "Viz_Description": {"element": "description", "qualifier": "viz"},
    "Parameters_01": {"element": "dqcheck", "qualifier": "requirement"},
    "Parameters_02": {"element": "dqcheck", "qualifier": "requirement"},
    "Parameters_03": {"element": "dqcheck", "qualifier": "requirement"},
    "Parameters_04": {"element": "dqcheck", "qualifier": "requirement"},
    "Parameters_05": {"element": "dqcheck", "qualifier": "requirement"},
    "Parameters_06": {"element": "dqcheck", "qualifier": "requirement"},
    "Parameters_07": {"element": "dqcheck", "qualifier": "requirement"},
    "Parameters_08": {"element": "dqcheck", "qualifier": "requirement"}
}

METADATA_TO_DSPACE_XML_MAPPING = {
    "Type": {"element": "entity", "qualifier": "type"}
}

DOMAIN_TO_COLLECTION_MAPPING ={
   "Quantitative Variable Distributions": "20.500.14642/1018",
}
