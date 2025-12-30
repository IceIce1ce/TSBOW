######################################
############ INSTRUCTIONS ############
######################################
# Select the data type that you need #
##### videos: .mp4 files
##### annotations: images & labels
######################################


REPO_ID='TSBOW'
OUT_DIR='NGOCHDM/Dataset/TSBOW/'

####################################
# Download "videos" only
####################################
python download_TSBOW.py        \
    --repo_id       $REPO_ID    \
    --output_dir    $OUT_DIR    \
    --type          'videos'
####################################


####################################
# Download "annotations" only
####################################
python download_TSBOW.py        \
    --repo_id       $REPO_ID    \
    --output_dir    $OUT_DIR    \
    --type          'annotations'
####################################