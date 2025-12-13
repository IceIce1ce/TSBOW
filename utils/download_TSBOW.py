import argparse
from huggingface_hub import hf_hub_download, snapshot_download

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
        choices=["videos", "annotations", "metadata", "all"],
        required=True,
        help="Type of data to download (videos, annotations, metadata, all)",
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        help="Local directory to save dataset",
        default="./TSBOW",
    )
    
    args = parser.parse_args()
    return  args


def main(args):
    print("Updating...")

    repo_id = f"SKKUAutoLab/{args.repo_id}"

    # Download csv metadata
    if args.type == "metadata":
        hub_paths = [
            # VIDEO_ID, SCENARIO, DAYTIME, WEATHER, SCALE, ROADTYPE, DURATION, FPS, ROI_DET, ROI_TRACK
            f"metadata/{args.repo_id}_info.csv",
            # VideoID for each attribute
            f"metadata/{args.repo_id}_listID.json"
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


    

if __name__ == "__main__":
    args    = parse_args()
    main(args=args)