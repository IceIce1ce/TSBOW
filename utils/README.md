# Instruction for the related files in utils


## Hugging Face


### download_TSBOW

The [download_TSBOW.py](download_TSBOW.py) provides the python source code for download our TSBOW dataset from Hugging Face. 

The download options are: *videos*, *annotations*, *metadata*, *semilabels*, *all*.
You can select one of them to download the data type.
- *videos*: &emsp;&emsp; &emsp;             the .mp4 files
- *annotations*:&emsp;         the manually labeled images and annotations
- *metadata*:&emsp;&emsp;                  the json file storing metadata
- *semilabels*: &emsp;&ensp;       the semi-labeled annotations (txt files)
- *all*: &emsp;&emsp;&emsp;&emsp;&emsp; all files and folders
<!-- &nbsp; 1 space     &ensp; 2 spaces -->
<!-- &emsp; 4 spaces     -->

The [download_TSBOW.py](download_TSBOW.py) can be executed via command:
```bash
python download_TSBOW.py                        \
    --repo_id       'TSBOW'                     \
    --output_dir    'NGOCHDM/Dataset/TSBOW/'    \
    --type          'all'
```

or run the [bash file](download_TSBOW.sh):
```bash
bash download_TSBOW.sh
```