####################################################################
########################### INSTRUCTIONS ###########################
####################################################################
# Select the data type that you need                               #
#  - videos: .mp4 files                 (official_release version) #
#  - annotations: images & labels       (official_release version) #
#  - metadata: json file                (official_release version) #
#  - semilabels: semi-labels            (official_release version) #
#  - official_release: split set according to frame_id             #
#  - camera_held_out: split set according to video_id              #
#  - all: all files and folders                                    #
####################################################################

# If lib:huggingface_hub is missing, run the command below to download `huggingface_hub` 
# !pip install huggingface_hub

REPO_ID='TSBOW'
OUT_DIR='NGOCHDM/Dataset/TSBOW/'


# Select one of types: 
##### (official_release)    videos, annotations, metadata, semilabels, comparison 
##### (data versions)       official_release, camera_held_out, all

DATA_TYPE='official_release'

python download_TSBOW.py        \
    --repo_id       $REPO_ID    \
    --output_dir    $OUT_DIR    \
    --type          $DATA_TYPE
