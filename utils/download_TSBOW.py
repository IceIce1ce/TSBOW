import argparse
from huggingface_hub import hf_hub_download, snapshot_download, login

DATASET_VERSIONS = {
    "official_release"  : "v1.0.0_official_release",
    "camera_held_out"   : "v1.1.0_camera_held_out",
}


def get_ignore_versions(data_version):
    ignore_list = []
    for version_name, version_full_name in DATASET_VERSIONS.items():
        if version_name != data_version:
            ignore_list.append(version_full_name)
    return ignore_list


# MARK: DOWNLOAD

def download_TSBOW(args):
    repo_id = f"SKKUAutoLab/{args.repo_id}"  #f"SKKUAutoLab/TSBOW/{args.repo_id}"


    # MARK: metadata
    # Download csv metadata
    if args.type == "metadata":
        hub_paths = [
            # SCENARIO, DAYTIME, WEATHER, SCALE, ROADTYPE, VIDEO_ID, DURATION, ROI
            f"metadata/{args.repo_id}_info.csv",
            # YAML file
            f"metadata/{args.repo_id}.yaml",

            # VideoID for each attribute
            # f"metadata/{args.repo_id}_listID.json"            
        ]

        for hub_path in hub_paths:
            hf_hub_download(
                repo_id         = repo_id,
                repo_type       = "dataset",
                filename        = hub_path,
                local_dir       = args.output_dir,
                resume_download = True,
            )
            print(f"Downloaded file '{hub_path}' from {repo_id} to {args.output_dir}")


    # MARK: videos
    # Download videos
    elif args.type == "videos":
        data_version_name = DATASET_VERSIONS["official_release"]
        
        # FOLDER: videos/
        # hub_paths = [
        #     f"{data_version_name}/train/videos/", 
        #     f"{data_version_name}/val/videos/"
        # ]
        
        # for hub_path in hub_paths:
        #     snapshot_download(
        #         repo_id=repo_id,
        #         repo_type="dataset",
        #         local_dir=f"{args.output_dir}/{hub_path}",
        #         allow_patterns=["*.mp4"],
        #     )
        #     print(f"Downloaded directory '{hub_path}' from {repo_id} to {args.output_dir}")

        # FILE: videos.zip
        hub_paths = [
            f"{data_version_name}/train/videos.zip", 
            f"{data_version_name}/val/videos.zip"
        ]

        for hub_path in hub_paths:
            hf_hub_download(
                repo_id         = repo_id,
                repo_type       = "dataset",
                filename        = hub_path,
                local_dir       = args.output_dir,
                resume_download = True,
            )
            print(f"Downloaded file '{hub_path}' from {repo_id} to {args.output_dir}")


    # MARK: annotations
    # Download annotations
    elif args.type == "annotations":
        # annotation.zip contains images/ and labels/ folders
        data_version_name = DATASET_VERSIONS["official_release"]
        hub_paths = [
            f"{data_version_name}/train/annotations.zip", 
            f"{data_version_name}/val/annotations.zip", 
            f"{data_version_name}/test_public/annotations.zip",

            f"{data_version_name}/train.txt", 
            f"{data_version_name}/val.txt", 
            f"{data_version_name}/test_public.txt",

            "classes.txt",
        ]

        for hub_path in hub_paths:
            hf_hub_download(
                repo_id         = repo_id,
                repo_type       = "dataset",
                filename        = hub_path,
                local_dir       = args.output_dir,
                resume_download = True,
            )
            print(f"Downloaded file '{hub_path}' from {repo_id} to {args.output_dir}")


    # MARK: semi-labels
    # Download semi-labels
    elif args.type == "semilabels":
        data_version_name = DATASET_VERSIONS["official_release"]
        hub_paths = [
            "classes.txt",
            f"{data_version_name}/train/semilabels.zip", 
            f"{data_version_name}/val/semilabels.zip"
        ]

        for hub_path in hub_paths:
            hf_hub_download(
                repo_id         = repo_id,
                repo_type       = "dataset",
                filename        = hub_path,
                local_dir       = args.output_dir,
                resume_download = True,
            )
            print(f"Downloaded file '{hub_path}' from {repo_id} to {args.output_dir}")


    # MARK: comp.
    # Download comparison set (4 scenes in [Experiments] datasets' comparison)
    elif args.type == "comparison":
        data_version_name = DATASET_VERSIONS["official_release"]
        hub_path = f"{data_version_name}/comparison.zip"
        hf_hub_download(
                repo_id         = repo_id,
                repo_type       = "dataset",
                filename        = hub_path,
                local_dir       = args.output_dir,
                resume_download = True,
            )
        print(f"Downloaded file '{hub_path}' from {repo_id} to {args.output_dir}")


    # MARK: camera_held_out
    # Download camera_held_out set
    elif args.type == "camera_held_out":
        data_version_name = DATASET_VERSIONS["camera_held_out"]
        hub_path = f"{data_version_name}/"

        snapshot_download(
            repo_id         = repo_id,
            repo_type       = "dataset",
            local_dir       = args.output_dir,
            allow_patterns  = [f"{hub_path}*"],
            resume_download = True,
        )
        print(f"Downloaded directory '{hub_path}' from {repo_id} to {args.output_dir}")

        hub_file_paths = [
            "classes.txt",
        ]
        for hub_file_path in hub_file_paths:
            hf_hub_download(
                repo_id         = repo_id,
                repo_type       = "dataset",
                filename        = hub_file_path,
                local_dir       = args.output_dir,
                resume_download = True,
            )
            print(f"Downloaded file '{hub_file_path}' from {repo_id} to {args.output_dir}")
    

    # MARK: official_release
    # Download official_release set
    elif args.type == "official_release":
        other_version_list = [
            f"{ignore_item}/"
            for ignore_item in get_ignore_versions(data_version="official_release")
        ]

        ignore_patterns = [
            f"{folder_name}/*"
            for folder_name in other_version_list
        ]

        snapshot_download(
            repo_id         = repo_id,
            repo_type       = "dataset",
            local_dir       = args.output_dir,
            ignore_patterns = ignore_patterns,
            resume_download = True,
        )
        print(f"Downloaded official release version from {repo_id} to {args.output_dir}")
    

    # MARK: all
    # Download entire dataset
    elif args.type == "all":
        snapshot_download(
            repo_id         = repo_id,
            repo_type       = "dataset",
            local_dir       = args.output_dir,
            resume_download = True,
        )
        print(f"Downloaded entire dataset from {repo_id} to {args.output_dir}")
    


# MARK: ARGUMENTS

def parse_args():
    # Setup command line arguments
    parser = argparse.ArgumentParser(
        description="Download TSBOW dataset from Hugging Face."
    )

    # The other versions of datasets will be added in the future
    parser.add_argument(
        "--repo_id",
        type=str,
        choices=["TSBOW"],
        required=True,
        help="Dataset type to download (TSBOW)",
    )

    parser.add_argument(
        "--type",
        type=str,
        choices=["videos", "annotations", "metadata", "semilabels", "comparison", "official_release", "camera_held_out", "all"],
        required=True,
        help="Type of data to download (videos, annotations, metadata, semilabels, comparison, official_release, camera_held_out, all)",
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        help="Local directory to save dataset",
        default="./TSBOW",
    )
    
    args = parser.parse_args()
    return  args



# MARK: MAIN

if __name__ == "__main__":
    args    = parse_args()

    # More details about login: 
    # https://huggingface.co/docs/huggingface_hub/quick-start#login
    login()
    
    download_TSBOW(args=args)