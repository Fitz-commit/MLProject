# Dataset Loader

This project provides a script `load.py` to load the dataset specified with MLCroissant. The dataset consists of various types of files including signal files, analysis data files, and YAML files.

The script is designed to automatically load each of the 113 samples in the dataset. Depending on your machine's capabilities, this process may take a while due to the size and complexity of the data.

## Customizing Data Loading

There are two ways to customize the loading process:

1. **Modify the script:** You can directly modify the `sample_ids`, `analysis_data_files`, and `yaml_data_files` lists in the script. For example:

    ```python
    sample_ids = ['sample1', 'sample2', 'sample3']
    ANALYSIS_DATA_FILES = ['AF.txt', 'Akt.txt']
    YAML_DATA_FILES = ['allgemeiner_schlaffragebogen_1.yml', 'arztbrief_1.yml']
    ```

2. **Pass arguments to the script:** You can pass arguments to the script when you run it. The script accepts the following arguments:

    - `--sample_ids`: A list of sample IDs to load. If not provided, all samples will be loaded.
    - `--analysis_data_files`: A list of analysis data files to load. If not provided, all analysis data files will be loaded.
    - `--yaml_data_files`: A list of YAML data files to load. If not provided, all YAML data files will be loaded.

    You can pass these arguments to the script like this:

    ```bash
    python load.py --sample_ids id1 id2 id3 --analysis_data_files file1.txt file2.txt --yaml_data_files file1.yml file2.yml
    ```

    In this command:

    - `python load.py` runs your script.
    - `--sample_ids id1 id2 id3` passes a list of sample IDs to your script.
    - `--analysis_data_files file1.txt file2.txt` passes a list of analysis data files to your script.
    - `--yaml_data_files file1.yml file2.yml` passes a list of YAML data files to your script.

    Each argument is separated by a space. If an argument value contains spaces, you should enclose it in quotes. For example, if a file name is `file 1.txt`, you would pass it as `"file 1.txt"`.


## Generating Statistics

You can generate visualized statistics for various YAML files using the `create_statistics.py` script.

To generate statistics for all YAML files, run the following command:

```bash
python create_statistics.py
```

This process will produce an HTML document stored inside a `reports` folder that presents the statistics for all samples. This document can be viewed and inspected in any web browser.

If you wish to generate statistics for specific YAML files only, you can specify them using the `--yaml_files` flag.

For example:

```bash
python create_statistics.py --yaml_files file_1.yml file_2.yml
```

Each file should be separated by a space. If a file name contains spaces, enclose it in quotes. For instance, if a file name is `file 1.yml`, you would pass it as `"file 1.yml"`.

Additionally, if you want to generate a separate report for each individual sample, you can use the `--individual_reports` flag. This will generate a unique report for each sample, which will be stored in the `individual_reports` subfolder within the `reports` directory.



```bash
python create_statistics.py --individual_reports
```

## Setup Environment

Before running the script, you need to set up your Python environment. Here are the steps to do so:

1. **Install Python:** Make sure you have Python 3.10 or later installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

2. **Create a virtual environment (optional):** It's recommended to create a virtual environment to isolate the dependencies for this project. You can create a virtual environment using the following command:

    ```bash
    python3 -m venv env
    ```

    Activate the virtual environment:

    - On Windows, run: `env\Scripts\activate`
    - On Unix or MacOS, run: `source env/bin/activate`

3. **Install dependencies:** Install the required Python libraries using pip. Run the following command:

    ```bash
    pip install -r requirements.txt
    ```

Make sure that the script `load.py` is palced in the directory containing the `data` folder, which holds the CPS dataset files and that this directory also contains the `utils.py`, `mappings.py`, and `croissant.json` files.

Now your environment is ready. You can run the script using the command `python load.py`.
