METADATA_TO_DUBLIN_XML_MAPPING = {
    "title": {"element": "title", "qualifier": "none"},
    "study_id": {"element": "title", "qualifier": "alternative"},

    "PI_01": {"element": "contributor", "qualifier": "author"},
    "PI_02": {"element": "contributor", "qualifier": "author"},

    "affiliation_01": {"element": "contributor", "qualifier": "other"},
    "affiliation_02": {"element": "contributor", "qualifier": "other"},

    "funder_01": {"element": "contributor", "qualifier": "none"},
    "funder_02": {"element": "contributor", "qualifier": "none"},

    "abstract": {"element": "description", "qualifier": "abstract"},
    "description": {"element": "description", "qualifier": "none"},

    "tags_01": {"element": "subject", "qualifier": "none"},
    "tags_02": {"element": "subject", "qualifier": "none"},
    "tags_03": {"element": "subject", "qualifier": "none"},
    "tags_04": {"element": "subject", "qualifier": "none"},
    "tags_05": {"element": "subject", "qualifier": "none"},
    "tags_06": {"element": "subject", "qualifier": "none"},

    "MeSH_01": {"element": "subject", "qualifier": "mesh"},
    "MeSH_02": {"element": "subject", "qualifier": "mesh"},
    "MeSH_03": {"element": "subject", "qualifier": "mesh"},
    "MeSH_04": {"element": "subject", "qualifier": "mesh"},
    "MeSH_05": {"element": "subject", "qualifier": "mesh"},
    "MeSH_06": {"element": "subject", "qualifier": "mesh"},
    "MeSH_07": {"element": "subject", "qualifier": "mesh"},
    "MeSH_08": {"element": "subject", "qualifier": "mesh"},
    "MeSH_09": {"element": "subject", "qualifier": "mesh"},
    "MeSH_10": {"element": "subject", "qualifier": "mesh"},

    "related_pub": {"element": "relation", "qualifier": "isreferencedby"},
    
    "publisher": {"element": "publisher", "qualifier": "none"},
    "rights": {"element": "rights", "qualifier": "none"},
    "license": {"element": "rights", "qualifier": "uri"}
}

METADATA_TO_DSPACE_XML_MAPPING = {
    "type": {"element": "entity", "qualifier": "type"}
}

METADATA_TO_LOCAL_XML_MAPPING = {
    "site_lead": {"element": "contributor", "qualifier": "siteLead"},
    "site_sponsor": {"element": "contributor", "qualifier": "siteSponsor"},
    "dev_code": {"element": "code", "qualifier": "github"},
    "admin_note": {"element": "admin", "qualifier": "note"},
    "grant": {"element": "contributor", "qualifier": "grant"},
    "participating_sites_01": {"element": "contributor", "qualifier": "sites"},
    "participating_sites_02": {"element": "contributor", "qualifier": "sites"},
    "participating_sites_03": {"element": "contributor", "qualifier": "sites"},
    "participating_sites_04": {"element": "contributor", "qualifier": "sites"},
    "participating_sites_05": {"element": "contributor", "qualifier": "sites"},
    "participating_sites_06": {"element": "contributor", "qualifier": "sites"},
    "participating_sites_07": {"element": "contributor", "qualifier": "sites"},
    "participating_sites_08": {"element": "contributor", "qualifier": "sites"},
    "participating_sites_09": {"element": "contributor", "qualifier": "sites"},
    "participating_sites_10": {"element": "contributor", "qualifier": "sites"},
    "participating_sites_11": {"element": "contributor", "qualifier": "sites"},
    "participating_sites_12": {"element": "contributor", "qualifier": "sites"}
}    

METADATA_TO_PROJECT_XML_MAPPING = {
    "start": {"element": "startDate", "qualifier": "none"},
    "end": {"element": "endDate", "qualifier": "none"}
}

DOMAIN_TO_THUMBNAIL_FILE_MAPPING = {
   "PEDSnet Projects": "STUDY.png",
   "PCORnet-Designated": "STUDY.png",
   "PEDSnet Nephrology Program": "STUDY.png",
   "PEDSnet Scholars": "STUDY.png",
   "PEDSnet Infrastructure": "STUDY.png"
 }

DOMAIN_TO_COLLECTION_MAPPING ={
   "PEDSnet Projects": "20.500.14642/42",
   "PCORnet-Designated": "20.500.14642/39",
   "PEDSnet Nephrology Program": "20.500.14642/679",
   "PEDSnet Scholars": "20.500.14642/822",
   "PEDSnet Infrastructure": "20.500.14642/40",
   "HIRR": "20.500.14642/1717",
}
