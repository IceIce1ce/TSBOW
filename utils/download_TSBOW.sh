######################################
############ INSTRUCTIONS ############
######################################
# Select the data type that you need #
#  - videos: .mp4 files              #
#  - annotations: images & labels    #
#  - metadata: json file             #
#  - semilabels: semi-labels         #
#  - all: all files and folders      #
######################################

REPO_ID='TSBOW'
OUT_DIR='NGOCHDM/Dataset/TSBOW/'

# Select one of types: videos, annotations, metadata, semilabels, comparison, all
DATA_TYPE='annotations'

python download_TSBOW.py        \
    --repo_id       $REPO_ID    \
    --output_dir    $OUT_DIR    \
    --type          $DATA_TYPE
