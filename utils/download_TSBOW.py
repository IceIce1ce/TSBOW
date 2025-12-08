import argparse
from huggingface_hub import hf_hub_download, snapshot_download

def main():
    print("Updating...")
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

if __name__ == "__main__":
    main()