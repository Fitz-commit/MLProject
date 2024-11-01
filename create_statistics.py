from load import load_analysis_and_yaml_files
from utils import get_question_mapping
import pandas as pd
from mlcroissant import Dataset
import sweetviz
import os
import argparse


sleep_duration = {"0Ah95Qw18puf1JsnrKBA6u8XXZLlMIQJ": 8.081, "0pdaTB9613iRUlhUJRAYvKmMQcOV3TYn": 7.353, "0vjSLbBj2sckqQam3tZ92QLDpQNYqaa0": 7.976, "1RLVk0ocGDZLI8RRhPglAc4I3gMSLqvu": 8.078, "1gQ3otWoJ3qNNJ5g4N1WtTC4JTFOlP9B": 8.667, "1vxo6QPCl4cn7JrPoKgTFUd6zZ6jrN6X": 7.486, "3DquDEk2YwjfckxNBAQuVTshrK3VWqO7": 8.228, "3rt8nhT9Ddda15KAPVhRXJgPcilmGipU": 8.304, "3veUj2KxK6jmJlllRj9tXbSncK6xnS0x": 8.314, "52JOaQM1ksTl9M7xo3AYi3Hto6exeWpG": 8.508, "5C1M33g2KLtBshvnj3V6S2MYFxbvFgbr": 8.828, "5Nl24yHOnojhw7nsgC0e530b2RBzOuLA": 7.809, "5mhIirR785Vve6LjBZyOqRviHmWUZl9M": 8.495, "5wPINWASVdhb63RK4DtJt5LuyuaWyMo8": 8.386, "80LORVUBBBcTBzaPxmmnfrlXC3bu3Dzw": 8.184, "8XdpUGiGQTqm1q6E1BiNZmYTcFwQovHP": 8.494, "9q7wGfr4xVuiodCCrqViuS1dnZ8tthvZ": 8.288, "A2YTNgCrkIoMGvSkyzK5R0EFgXVRfptP": 7.583, "AEhNZrB5mb9K7hCBxB0xvJzUC5WxqaFN": 8.364, "AavMakHhFeoHz9AgdWVTBsXCdiOLBNEk": 7.132, "Adm1jCIZpVR5Evov0BZ5XyEA3QXgkpiO": 8.63, "Bmy6KwUhfqRDp6bzRx1PaWoQvBpImF01": 6.55, "C2Lt7JOOpGRwdu2TrCMDNn1jE8nBCHpb": 8.179, "CMTsL0EWEJvQqMe0GKKCKN87IXp9L0UU": 7.784, "CzwqE37s81YahjNICSXI2Tb4Fmp6bclE": 8.453, "DlUvX2vg1c4ORh63BRFaCxbMlr8DeCbO": 7.646, "F8Uu1bz0NcullMqx3o7S1o3M4VRg7EtR": 7.127, "FLsgQZoIGHx1G3LmdD7jtICMik2EKRKN": 8.334, "FPSnBoS217CEJ8cZS7MO3VuYUJwIt8LV": 8.511, "FRU8DMa3f1esZLFfzixxhgJk0KvG7vXX": 8.055, "FddiLTFWMZFHH5s1NFddllezef4BJhwS": 7.583, "GJShIRZ3lsuqeG7HhgpwlMw5v8prIuD4": 7.471, "HeeJJy8N63XTT1mmruOcaXwl9gH06LLR": 8.132, "HvVu33fnVKDLLjwY8Mtytcgi8Btsr1kS": 8.335, "I4PBCtY88EMiljTpJ6ns5kIoimlIUgfl": 7.783, "INzmELsQB5yeF6HnHRM76U1ufVy7vmfb": 7.838, "JyXyuQIuFyAtKL8ZoWS98xvpW4PJFco6": 8.111, "KB84bUmLWOrKCKkISCn8QuNBhF5mg0L8": 8.385, "KBn6Fz4XRNh5A7YRBBGZIlSVzcmV6P51": 8.884, "KIdPVCRCkXIaWDQ4c4gU38xpH5PAnOSV": 7.652, "KX83zwqAkUKsTWQKeWmfjewObf8y7upu": 8.674, "KkgHbcRejP3vgmwPVpI3jW3Pq6cddRsJ": 7.42, "LcsapTberZwzU7qyEr11andO59HTOVCv": 6.518, "M7d3C4ZQtx0R00Wum7JMxQtZExUfNEzi": 6.683, "MT1zW5iB0h1bxF42QBpyDqotQk7NcnHw": 7.556, "MT9Dkn3L0akMVov0lRUq9HmNsP49R1dX": 9.034, "MYzsHdeN4rEc6ne1SobyUoK2u2bedJUp": 7.984, "MyE1OSaDFTs03JE5K1CLusYomSaDFufz": 7.245, "OCi1DrQQgJ7GjNFNTrxscclxkaDH0Y76": 8.757, "Oa7cBsB7PQPy7Kr8jHkJorml61mv4kIP": 8.849, "P45k7fhnHTEWYkEMfEPSAK2tp2hizA7O": 8.062, "PK0t8NcGbxRcfL8tTxbrdxJe6zY1WS9f": 7.429, "Pk9lFIEExot3gjvV83ZDTuWSj6dqk9uW": 8.104, "QHauJpImWK54mPysmthbCSRI6BwQfuim": 7.429, "RhDBHQQCPFEvVYagp1SorSLbEygFUiAL": 8.393, "RpARZ17l5osnFUcqIj2aTOsgRBMDutoA": 6.394, "RqC1HNwuWs5fhqEheSYlRc93EoReggVm": 7.905, "S8dOGQgMx9WOH90orySWSfGuBL2mpxgC": 8.428, "Su02hndUSYGSKJmcSqroKmtDjXIJ4y60": 8.405, "TLYaLIWCrBbtqLySvqxj67g5ZAfn2Zhs": 6.688, "U2onxpoiCTT2F4SHmDMTeWb2GgWtRZhb": 8.411, "UldfKBDGVlNpqUbcVPLV68eOFqucUj06": 8.329, "Vth5VKxswvoQEpLCis200xjS0f0ctjFu": 8.369, "XSedsGunPd3IUuZ8RJUGmz3SUoCv0rzW": 7.615, "XpSmjNEW0Mad8655KQ4q3NjDHNUNHW6C": 8.241, "YFQX33c8EEoapTndd2084KbUuUmtj7xF": 9.076, "Yp6NRNtFSjbjdcFWN7Q1ATwOir9wrBNw": 7.469, "ZFkXoBHziu00Toye78g1YdKm5P0bA0dY": 8.019, "ZizO4wnchcm4tTOACaPUrkRtopGIjkFq": 7.984, "ZwojnSyDEhD6s8ZERY8AoDWL0cnBH7BU": 7.851, "dxAGfKahLvCc0GhMyac32CmQo10JGLuF": 7.443, "eX0CkhjYbsXlnwQwAHsFDo9XyPV9b7oj": 8.306, "euzXQcpDnB1xsKeKOJHYW48lSNZXiVHK": 8.137, "gm7PhGPwaWaEeOoG0lK0altS9tLOBYGt": 6.974, "hOwipKAoUqK6vJDqsjnchMKZf0e9uSH8": 8.307, "hrBQwXe1RNG3VJXIAQAgC7JAjl2XlHyD": 8.411, "ip25KNFw4RbDNeQTXjLI95OsnQLLe35e": 7.81, "jusHjPORbNBFg6iMvaNE4HcFMc4oJyqD": 6.699, "kKDzUlAprXqDz84Nrw9UP1W0jpgUKkhN": 8.55, "kxrBCJhec2Aub2FmnrU1dCIx7f3HlST6": 8.305, "l1VJ9A1olk859kfiGM7UNdjqitFHl3fa": 8.966, "leySrSnra9yAO3eTJIGB55nrjRS3RqIW": 7.66, "mXHZZ887A9fcZgOmnxhnPVHwu5ECljDG": 7.844, "mkcvU3fDfRGULYMwqm0FCUlqPTzrSb8P": 8.629, "niVBznqEcE3RfyWa2u7EXjpguXBMB9dE": 8.595, "nozzxBTVeanjyN8aDAOknM5gv55sydOG": 8.357, "nrtZyE7IBmlm0ZH3gG7FHJAoYxlFqczB": 7.277, "oEJ7fslCTL7s0OfIe7nYIPqo7Il4rMjI": 8.169, "oTlKy2ISbZfN7i2jTcZ4mCqmCpK6dhDm": 6.302, "pY4EUZQszT0kL5Et76FkEbRlLeAMT2hz": 8.435, "rHg2gQNoevGYPUag6PAn9CANXKmx17ms": 8.258, "rYbtzQzJJVg8Wksx9dU8wHg2X1R8zulJ": 7.216, "rxODabL5H6LkFhXhov0iCYKaxTA9SKSY": 7.161, "sUDb7jmMMO6h7QCGGbkwa7LRv1JYu8hy": 7.184, "srARDl4a3Z4Gtb39GTOv0ynNVE6T7xHS": 7.96, "ssRHUDqjbEgtepnEnjPpOd6WQHekD6PZ": 8.458, "t1dRq19eE7PizNhNBod8AT5pX18KFAul": 7.528, "tIgyhF8T1BOZnu7h6jb58igU5MAGgdo9": 7.314, "tU3dZpxIdmbr9wpPpFeZGh5MciOB1TgT": 7.274, "tfAnzkFia5hzaA6bHYFpkj3jPF90FzAj": 7.777, "tihrah4T4i2gA8dscroj9Mu5715fXojg": 8.101, "vHJMSYFIl1TfLweQ5DWMGN5f47ULFNxe": 7.921, "vc3ShhPeF5CiTm9Hi0moakicyNWNulab": 7.939, "vvcikOyQkXvfZdNkFYEWveZjUlQmYrSf": 8.298, "wl5eUqFCFGibvn13l8axb82mNOkp0doc": 8.467, "wuxfEVb6iJ7GghVUjN5eKTO0VsulXaOg": 8.013, "x6nbOt0fqHhNHbYCgQP0Eaa7ymp6eKuq": 7.215, "xc54eJI7x5BwwtOLSfdRnYdvMLagr1sp": 7.942, "xijlZSyZXb5MEfbKLM54iOJRJkRdrBrX": 6.753, "yAP2PJs1dDSFdYXe6GrQtQC7iO8oyX3L": 8.5, "yWLp2YwYQlKqoSR14JUiazZzcywX8Xj8": 7.156, "zWtiCjFSxBFRmU3DklC4UMFKFHCOXJgS": 7.232, "zjSqovtw62tjDA2tSelpFpAvfXbGUyI5": 7.838}




nan_list = []

# Questions that are too long, and ruin some of the readability of the report
long_question_list = []


def get_number_apnoe_hypopnoe(event_data):

    count_apnoe = 0
    count_hypopnoe = 0
    for line in event_data:
        if 'Apnoe' in line[3]:
            count_apnoe += 1
        elif 'Hypopnoe' in line[3]:
            count_hypopnoe += 1

    return count_apnoe, count_hypopnoe

def extract_arztbrief(data):
    """
    Extracts the relevant data from the arztbrief
    """

    hasBaveno = False
    hasT90 = False

    tmp = data['Sleep medical diagnosis'].split(',')
    arztdata = {}
    for string in tmp:
        if 'Baveno-Klassifikation:' in string:
            arztdata['Baveno-Classification'] = string.split(': ')[1]
            hasBaveno = True
        elif 'T90:' in string:
            arztdata['T90'] = string.split(': ')[1]
            hasT90 = True
    # Schlafmedizinische Diagnose(n) is always the first element
    lastIndex = -2 if hasBaveno and hasT90 else -1 if hasBaveno or hasT90 else None

    arztdata['Sleep medical diagnosis'] = ",".join(tmp[0:lastIndex])
    return arztdata

def prepare_data(base_path, sample_ids, yaml_statistic_files):

    analysis_data, yaml_data = load_analysis_and_yaml_files(base_path, sample_ids)
    yaml_data = get_question_mapping(yaml_data)
    
    if not all(file in yaml_data[sample_ids[0]].keys() for file in yaml_statistic_files):
        exit("YAML data does not contain necessary files to analyze the data, make sure to include the files specified in yaml_statistic_files.")

    # Reduce data to selected files and transform int to str, to have consistent data types
    yaml_statistic_data = {
        sample_id: {
            k: str(v) if isinstance(v, int) else v 
            for yaml_file, content in yaml_dict.items() 
            if yaml_file in yaml_statistic_files 
            for k, v in content.items()
        } 
        for sample_id, yaml_dict in yaml_data.items()
    }

    # Check if analysis data contains necessary files to calculate the AHI and ARI
    necessary_files = ['Effort Ext1 Events.txt', 'Effort Ext2 Events.txt', 'Flow Events.txt', 'Klassifizierte Arousal.txt']
    if not all(file in analysis_data[sample_ids[0]].keys() for file in necessary_files):
        exit("Analysis data does not contain necessary files to calculate the AHI and ARI, make sure to include the following files: 'Effort Ext1 Events.txt', 'Effort Ext2 Events.txt', 'Flow Events.txt', 'Klassifizierte Arousal.txt'")

    for sample_id in yaml_statistic_data.keys():

        # Add Number of Arousals Events to the data
        number_of_arousals = len(analysis_data[sample_id]['Klassifizierte Arousal.txt'])
        yaml_statistic_data[sample_id]['number_of_arousals'] = number_of_arousals

        # Extract the relevant data from the arztbrief
        yaml_statistic_data[sample_id].update(extract_arztbrief(yaml_data[sample_id]['arztbrief_1.yml']))

        sleep_duration_hours = sleep_duration[sample_id]
        # Add AHI (Apnoe-Hypopnoe-Index) / ARI to the data
        number_apnoe_ext_1, number_hypopnoe_ext_1 = get_number_apnoe_hypopnoe(analysis_data[sample_id]['Effort Ext1 Events.txt'])
        yaml_statistic_data[sample_id]['AHI_Ext_1'] = (number_apnoe_ext_1 + number_hypopnoe_ext_1) / sleep_duration_hours

        number_apnoe_ext_2, number_hypopnoe_ext_2 = get_number_apnoe_hypopnoe(analysis_data[sample_id]['Effort Ext2 Events.txt'])
        yaml_statistic_data[sample_id]['AHI_Ext_2'] = (number_apnoe_ext_2 + number_hypopnoe_ext_2) / sleep_duration_hours

        number_apnoe_flow,  number_hypopnoe_flow = get_number_apnoe_hypopnoe(analysis_data[sample_id]['Flow Events.txt'])
        yaml_statistic_data[sample_id]['AHI_Flow'] = (number_apnoe_flow + number_hypopnoe_flow) / sleep_duration_hours

        yaml_statistic_data[sample_id]['AHI'] = (
            number_apnoe_ext_1 + number_hypopnoe_ext_1 + number_apnoe_ext_2 +
            number_hypopnoe_ext_2 + number_apnoe_flow +
            number_hypopnoe_flow) / sleep_duration_hours
        
        # Add ARI to the data
        yaml_statistic_data[sample_id]['ARI'] = number_of_arousals / sleep_duration_hours

    # Create DataFrame
    df = pd.DataFrame(yaml_statistic_data).T
    df = df.infer_objects()

    return df

def create_report():

    yaml_statistic_files = [
        'allgemeiner_schlaffragebogen_1.yml',
        'allgemeiner_schlaffragebogen_1_2.yml',
        'epworth_sleepiness_scale.yml',
        'psqi_fragebogen_1.yml',
        'psqi_fragebogen_2.yml',
        'psqi_fragebogen_3.yml',
        'psqi_fragebogen_4.yml',
        'restless_legs_fragebogen.yml'
    ]

    # Setup arguments
    parser = argparse.ArgumentParser(description='Create statistics report.')
    parser.add_argument('--yaml_files', nargs='*', default=yaml_statistic_files, help='A list of YAML files to use for statistics.')
    parser.add_argument('--individual_reports', action='store_true', help='Generate individual reports for each sample')

    args = parser.parse_args()

    yaml_statistic_files = args.yaml_files

    dataset = Dataset(jsonld="croissant.json")

    base_path = dataset.metadata.url
    directory = os.path.dirname(__file__)
    base_path = os.path.join(directory, base_path)
    sample_ids = os.listdir(base_path)

    data = prepare_data(base_path, sample_ids, yaml_statistic_files)
    
    #feature_config = sweetviz.FeatureConfig(force_num=['number_of_arousals'])
    report = sweetviz.analyze([data, "CPS Dataset"])

    # Save the overview report
    os.makedirs('reports', exist_ok=True)
    report.show_html('reports/overview.html')

    # Create a report for each sample
    create_single_reports = args.individual_reports
    if create_single_reports:
        os.makedirs('reports/individual_reports', exist_ok=True)
        for sample_id in sample_ids:
            sample_df = pd.DataFrame(data.loc[sample_id]).T
            report = sweetviz.analyze([sample_df, f"CPS Dataset, {sample_id}"])
            report.show_html(f'reports/individual_reports/{sample_id}.html', open_browser=False)

create_report()
