import pandas as pd
import os
import shutil
import click
import warnings
import xml.etree.ElementTree as ET
from assets.mappings import METADATA_TO_DUBLIN_XML_MAPPING, DOMAIN_TO_THUMBNAIL_FILE_MAPPING, DOMAIN_TO_COLLECTION_MAPPING
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
        df = pd.read_excel(excel_path)
    for index, row in df.iterrows():
        row_dict = row.to_dict()
        curr_result_path = os.path.join(results_path, run_id, 'Item_'+str(index).zfill(3))
        # copy csv
        csv_file_path = os.path.join(csv_base_path, row_dict['filename'])
        os.mkdir(curr_result_path)
        shutil.copy(csv_file_path, curr_result_path)
        # generate xml
        root = ET.Element("dublin_core")
        for key, value in METADATA_TO_DUBLIN_XML_MAPPING.items():
            element = value['element']
            qualifier = value['qualifier']
            text_value = row_dict[key]
            dcvalue = ET.SubElement(root, "dcvalue")
            dcvalue.set("element", element)
            dcvalue.set("qualifier", qualifier)
            dcvalue.text = text_value
        tree = ET.ElementTree(root)
        ET.indent(tree)
        tree.write(os.path.join(curr_result_path, "dublin_core.xml"), encoding="UTF-8", xml_declaration=True)
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
        # generate contents
        with open(os.path.join(curr_result_path, 'contents'), 'w') as f:
            f.write(f'{row_dict['filename']}\n{DOMAIN_TO_THUMBNAIL_FILE_MAPPING[row_dict['Domain']]}\tbundle:THUMBNAIL')

if __name__ == '__main__':
    bulk_deposit()
