**Python Synthetic Data Generator** (`pysdg`) is a powerful tool for generating synthetic tabular datasets using various machine learning algorithms. 

The `pysdg` package is developed by the [Electronic Health Information Laboratory (EHIL)](https://www.ehealthinformation.ca/) at the [CHEO Research Institute](https://www.cheori.org/). It is designed to facilitate the generation of synthetic data for clinical trials, enabling various types of analyses. The package ensures consistency and robustness in handling different clinical trial datasets and generative models. 

### Documentation

Comprehensive documentation for the latest version of `pysdg` is available at [pysdg documentation](https://cheo-ehil.github.io/pysdg-releases/latest/index.html).

### Installation

You can install the package by using the appropriate release wheel file available in this repository. First, set up the virtual environment as detailed in the documentation. After downloading the wheel file, you can install it using pip. For example, to install `pysdg` v2.7.0, run:

```bash
pip install pysdg-2.7.0-py3-none-any.whl
```

Alternatively, you can download the relevant Docker image from [pysdg in Jupyter](https://github.com/orgs/CHEO-EHIL/packages/container/package/pysdg%2Fpy) for `Python` users and from [pysdg in RStudio](https://github.com/orgs/CHEO-EHIL/packages/container/package/pysdg%2Fr) for `R` users.

To install and use the test Docker image, ensure Docker is installed on your machine. For example, to use the latest version of the `pysdg` library in a Jupyter notebook, follow these steps:

```bash
docker pull ghcr.io/cheo-ehil/pysdg/py:latest
docker run -p 8888:8888 -v /your/local/directory:/home/jovyan/data --name your-pysdg-image-name ghcr.io/cheo-ehil/pysdg/py:latest
```

After executing these commands, follow the provided link to access the container via your web browser. Next, you can copy the tutorial files from the repository to your mapped /your/local/directory to start exploring `pysdg`.

You can also find an RStudio-based image in the same link to the packages.

For any inquiries or support, please open an issue in this repository.

<p align="center">
  <img alt="EHIL-CHEO Logos" src="docs/images/ehil_cheo.png" width="600" style="margin-right: 40px;">
</p>
