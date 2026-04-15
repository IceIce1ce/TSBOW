# Instruction for the related files in utils


<!-- MARK: Hugging Face -->

## Hugging Face


### download_TSBOW

The [download_TSBOW.py](download_TSBOW.py) provides the python source code for download our TSBOW dataset from Hugging Face. 

The download options are: *videos*, *annotations*, *metadata*, *semilabels*, *comparison*, *all*.
You can select one of them to download the data type.
- *videos*: &emsp;&emsp; &emsp;             the .mp4 files
- *annotations*:&emsp;         the manually labeled images and annotations
- *metadata*:&emsp;&emsp;                  the json file storing metadata
- *semilabels*: &emsp;&ensp;       the semi-labeled annotations (txt files)
- *comparison*:&emsp;         the manually labeled images and annotations for Datasets' Comparison in Experiments
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

**Library requirement**: `huggingface_hub`

```
!pip install huggingface_hub
```


**Notes:** 
The first public version, we only provide 30% of the test set.



<!-- MARK: Citation -->

## 🏅 Citation

**If our research is helpful to you, please cite our paper using the following BibTeX format**

```bibtex
@article{Huynh2026TSBOW, 
    title={TSBOW: Traffic Surveillance Benchmark for Occluded Vehicles Under Various Weather Conditions}, 
    author={Huynh, Ngoc Doan-Minh and Tran, Duong Nguyen-Ngoc and Pham, Long Hoang and Tran, Tai Huu-Phuong and Jeon, Hyung-Joon and Nguyen, Huy-Hung and Khac Vu, Duong and Jeon, Hyung-Min and Phan, Son Hong and Pham-Nam Ho, Quoc and Tran, Chi Dai and Khanh, Trinh Le Ba and Jeon, Jae Wook}, 
    journal={Proceedings of the AAAI Conference on Artificial Intelligence}, 
    volume={40}, 
    number={7}, 
    url={https://ojs.aaai.org/index.php/AAAI/article/view/37439}, 
    DOI={10.1609/aaai.v40i7.37439}, 
    year={2026}, 
    month={Mar.}, 
    pages={5239-5247} 
}
```