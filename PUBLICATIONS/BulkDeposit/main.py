import pandas as pd
import os
import shutil
import click
import warnings
import xml.etree.ElementTree as ET
from assets.mappings import METADATA_TO_DUBLIN_XML_MAPPING, DOMAIN_TO_COLLECTION_MAPPING, METADATA_TO_DSPACE_XML_MAPPING, DOMAIN_TO_THUMBNAIL_FILE_MAPPING
from datetime import datetime

@click.command()
@click.option(
    '--excel_path', 
    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True), 
    required=True,
    help='path to metadata excel file'
)
@click.option(
    '--csv_base_path', 
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True), 
    required=True,
    help='path to dir that holds codeset csv files'
)
@click.option(
    '--results_path', 
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True), 
    required=True,
    help='path to store results'
)
def bulk_deposit(excel_path, csv_base_path, results_path):
    run_id = datetime.now().strftime("%Y%m%d%H%M%S")
    click.echo("run_id: " + run_id)
    os.mkdir(os.path.join(results_path, run_id))
    with warnings.catch_warnings(action='ignore', category=UserWarning):
        df = pd.read_excel(excel_path, dtype=str).fillna('')
    for index, row in df.iterrows():
        row_dict = row.to_dict()
        curr_result_path = os.path.join(results_path, run_id, 'Item_'+str(index).zfill(3))
    
    # create result directory
    os.mkdir(curr_result_path)
    
    # copy csv only if filename exists
    if row_dict['filename'] and row_dict['filename'].strip():
        csv_file_path = os.path.join(csv_base_path, row_dict['filename'])
        shutil.copy(csv_file_path, curr_result_path)
        
        # generate dublin_core.xml
        root = ET.Element("dublin_core")
        for key, value in METADATA_TO_DUBLIN_XML_MAPPING.items():
            element = value['element']
            qualifier = value['qualifier']
            text_value = row_dict[key]
            try:
                parsed_date = pd.to_datetime(text_value, errors='raise')
                text_value = parsed_date.strftime('%Y-%m-%d')
            except Exception:
                pass
            dcvalue = ET.SubElement(root, "dcvalue")
            dcvalue.set("element", element)
            dcvalue.set("qualifier", qualifier)
            dcvalue.text = text_value
        tree = ET.ElementTree(root)
        ET.indent(tree)
        tree.write(os.path.join(curr_result_path, "dublin_core.xml"), encoding="UTF-8", xml_declaration=True)
        
        # generate metadata_dspace.xml
        root = ET.Element("dublin_core", schema="dspace")
        for key, value in METADATA_TO_DSPACE_XML_MAPPING.items():
            element = value['element']
            qualifier = value['qualifier']
            text_value = row_dict[key]
            dcvalue = ET.SubElement(root, "dcvalue")
            dcvalue.set("element", element)
            dcvalue.set("qualifier", qualifier)
            dcvalue.text = text_value
        tree = ET.ElementTree(root)
        ET.indent(tree)
        tree.write(os.path.join(curr_result_path, "metadata_dspace.xml"), encoding="UTF-8", xml_declaration=True)
        
        # generate metadata_local.xml
        #root = ET.Element("dublin_core", schema="local")
        #for key, value in METADATA_TO_LOCAL_XML_MAPPING.items():
        #    element = value['element']
        #    qualifier = value['qualifier']
        #    text_value = row_dict[key]
        #    dcvalue = ET.SubElement(root, "dcvalue")
        #    dcvalue.set("element", element)
        #    dcvalue.set("qualifier", qualifier)
        #    dcvalue.text = text_value
        #tree = ET.ElementTree(root)
        #ET.indent(tree)
        #tree.write(os.path.join(curr_result_path, "metadata_local.xml"), encoding="UTF-8", xml_declaration=True)
        
        # copy thumbnail
        thumbnail_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 
            'assets/thumbnail', 
            DOMAIN_TO_THUMBNAIL_FILE_MAPPING[row_dict['Domain']]
        )
        shutil.copy(thumbnail_path, curr_result_path)

        # generate collections
        collections_text = DOMAIN_TO_COLLECTION_MAPPING[row_dict['Domain']]
        with open(os.path.join(curr_result_path, 'collections'), 'w') as f:
            f.write(collections_text)

        # generate contents (blank if no filename)
        with open(os.path.join(curr_result_path, 'contents'), 'w') as f:
            if row_dict['filename'] and row_dict['filename'].strip():
                f.write(row_dict['filename'])
            else:
                f.write('')  # write empty string to create blank file
if __name__ == '__main__':
    bulk_deposit()
