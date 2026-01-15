import argparse
from huggingface_hub import hf_hub_download, snapshot_download, login


# MARK: Download

def download_TSBOW(args):
    print("Updating...")

    repo_id = f"SKKUAutoLab/{args.repo_id}"  #f"SKKUAutoLab/TSBOW/{args.repo_id}"


    # Download csv metadata
    if args.type == "metadata":
        hub_paths = [
            # SCENARIO, DAYTIME, WEATHER, SCALE, ROADTYPE, VIDEO_ID, DURATION, ROI
            f"metadata/{args.repo_id}_info.csv",

            # VideoID for each attribute
            # f"metadata/{args.repo_id}_listID.json"

            # YAML and TXT files for training
            f"metadata/{args.repo_id}.yaml",
            f"metadata/train.txt",
            f"metadata/val.txt",
            f"metadata/test_public.txt",
        ]

        for hub_path in hub_paths:
            hf_hub_download(
                repo_id=repo_id,
                repo_type="dataset",
                filename=hub_path,
                local_dir=args.output_dir,
                resume_download=True,
            )
            print(f"Downloaded file '{hub_path}' from {repo_id} to {args.output_dir}")


    # Download videos
    elif args.type == "videos":
        # FOLDER: videos/
        # hub_paths = ["train/videos/", "val/videos/"]
        
        # for hub_path in hub_paths:
        #     snapshot_download(
        #         repo_id=repo_id,
        #         repo_type="dataset",
        #         local_dir=f"{args.output_dir}/{hub_path}",
        #         allow_patterns=["*.mp4"],
        #     )
        #     print(f"Downloaded directory '{hub_path}' from {repo_id} to {args.output_dir}")

        # FILE: videos.zip
        hub_paths = ["train/videos.zip", "val/videos.zip"]

        for hub_path in hub_paths:
            hf_hub_download(
                repo_id=repo_id,
                repo_type="dataset",
                filename=hub_path,
                local_dir=args.output_dir,
                resume_download=True,
            )
            print(f"Downloaded file '{hub_path}' from {repo_id} to {args.output_dir}")


    # Download annotations
    elif args.type == "annotations":
        # annotation.zip contains images/ and labels/ folders
        hub_paths = ["train/annotations.zip", "val/annotations.zip", "test_public/annotations.zip"]

        for hub_path in hub_paths:
            hf_hub_download(
                repo_id=repo_id,
                repo_type="dataset",
                filename=hub_path,
                local_dir=args.output_dir,
                resume_download=True,
            )
            print(f"Downloaded file '{hub_path}' from {repo_id} to {args.output_dir}")


    # Download semi-labels
    elif args.type == "semilabels":
        hub_paths = ["train/semilabels.zip", "val/semilabels.zip"]

        for hub_path in hub_paths:
            hf_hub_download(
                repo_id=repo_id,
                repo_type="dataset",
                filename=hub_path,
                local_dir=args.output_dir,
                resume_download=True,
            )
            print(f"Downloaded file '{hub_path}' from {repo_id} to {args.output_dir}")

    # Download comparison set (4 scenes in [Experiments] datasets' comparison)
    elif args.type == "comparison":
        hub_path = "comparison.zip"
        hf_hub_download(
                repo_id=repo_id,
                repo_type="dataset",
                filename=hub_path,
                local_dir=args.output_dir,
                resume_download=True,
            )
        print(f"Downloaded file '{hub_path}' from {repo_id} to {args.output_dir}")

    # Download entire dataset
    elif args.type == "all":
        snapshot_download(
            repo_id=repo_id,
            repo_type="dataset",
            local_dir=args.output_dir,
            resume_download=True,
        )
        print(f"Downloaded entire dataset from {repo_id} to {args.output_dir}")
    


# MARK: Args

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
        choices=["videos", "annotations", "metadata", "semilabels", "comparison", "all"],
        required=True,
        help="Type of data to download (videos, annotations, metadata, semilabels, comparison, all)",
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        help="Local directory to save dataset",
        default="./TSBOW",
    )
    
    args = parser.parse_args()
    return  args



# MARK: Main

if __name__ == "__main__":
    # More details about login: https://huggingface.co/docs/huggingface_hub/quick-start#login
    login()

    args    = parse_args()
    download_TSBOW(args=args)