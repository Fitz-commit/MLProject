import yaml
from mappings import mappings
import json

def read_event_file_as_list(file_path):
    """
    reads the event file and returns a list of lists.
    each list depends on the type of event file.
    returns None if the file is not found.
    """
    file_as_list = []
    events_list = []
    type_of_file = ""

    load_file = open(file_path, "r", encoding="iso-8859-1")
    for line in load_file:
        if not line.strip():
            continue  # skip the empty line
        current_full_line = line.strip()
        if "Events list" in current_full_line.split(":"):
            # turn the string of event types into a list
            events_list = current_full_line.split(":")[1].strip().split(
                ",")

            # remove elements that exist multiple times
            events_list = list(dict.fromkeys(events_list))
        elif "Rate" in current_full_line.split(":"):
            pass
        elif "Start Time" in current_full_line.split(":"):
            pass
        elif "Signal ID" in current_full_line.split(":"):
            pass
        elif "Signal Type" in current_full_line.split(":"):
            type_of_file = current_full_line.split(":")[1].strip()
            pass
        elif "Unit" in current_full_line.split(":"):
            pass
        elif "wnit" in current_full_line.split(":"):
            pass
        elif " A" in current_full_line.split(":"):
            pass
        else:
            split_line = current_full_line.split(";")
            if type_of_file == "Impuls":
                start_end_time = split_line[0].strip().split("-")
                file_as_list.append([
                    start_end_time[0].strip(),
                    start_end_time[1].strip(),
                    float(split_line[1].strip().replace(',', '.')),
                    split_line[2].strip(),
                ])
            elif type_of_file in ['Discret', 'Analog']:
                file_as_list.append([
                    split_line[0].strip(),
                    split_line[1].strip(),
                ])
            else:
                pass

    load_file.close()

    return file_as_list, type_of_file, events_list

def yml_import(path):

    with open(path, "r") as f:
        try:
            data = yaml.load(f, Loader=yaml.SafeLoader)
        except yaml.YAMLError as e:
            raise e
    return data

def get_question_mapping(yaml_data):
    question_mapping = {}

    for sample_id, yaml_dict in yaml_data.items():
        question_mapping[sample_id] = {}
        for yaml_file, yaml_content in yaml_dict.items():
            if yaml_file in mappings:
                question_mapping[sample_id][yaml_file] = {mappings[yaml_file].get(key, key): value for key, value in yaml_content.items()}

    return question_mapping
