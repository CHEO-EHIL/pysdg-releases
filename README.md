**Python Synthetic Data Generator** (`pysdg`) is a robust synthetic data generator for tabular datasets incorporating different types of ML-based generation algorithms. The invaluable tool also comprises add-ons to calculate privacy risks and others.

`pysdg` is designed by the [Electronic Health Information Laboratory (EHIL)](https://www.ehealthinformation.ca/) at the [CHEO Research Institute](https://www.cheori.org/). The package is meant to streamline the generation of synthetic data for clinical trials and support various types of analyses. It ensures consistency and robustness when handling different clinical trial datasets and generative models. The package acts as a wrapper for several reliable generative modeling implementations and includes two modules: `synth` and `privacy`.

### Documentation  
The full documentation can be found at [pysdg documentation](https://cheo-ehil.github.io/pysdg-releases/).

### Installation

You have the option to install the package by using the appropriate release wheel file available in this repository, following the installation instructions provided in the relevant release documentation linked above. Alternatively, you can download the corresponding image from [CHEO-EHIL Packages](https://github.com/orgs/CHEO-EHIL/packages).

For instance, to install and utilize the most recent Docker image, ensure that Docker is set up on your machine. Then, execute the following commands in your terminal:

```bash
docker pull ghcr.io/cheo-ehil/technical-resources-and-docs/ehil-py-pysdg:latest
docker run -p 8888:8888 -v /your/local/directory:/home/jovyan/data --name your-pysdg-image-name ghcr.io/cheo-ehil/technical-resources-and-docs/ehil-py-pysdg:latest
```
After executing these commands, follow the provided link to access the container via your web browser. Next, you can copy the tutorial files from the repository to your mapped /your/local/directory to start exploring `pysdg`.

Please note that the tutorial files are produced using the latest version (even if it beta version).

For any questions, please submit an issue in this repository.

<p align="center">
  <img alt="EHIL-CHEO Logos" src="docs/images/ehil_cheo.png" width="600" style="margin-right: 40px;">
</p>
