**Python Synthetic Data Generator** (`pysdg`) is a powerful tool for generating synthetic tabular datasets using various machine learning algorithms. It also includes additional features for assessing privacy risks and more.

The `pysdg` package is developed by the [Electronic Health Information Laboratory (EHIL)](https://www.ehealthinformation.ca/) at the [CHEO Research Institute](https://www.cheori.org/). It is designed to facilitate the generation of synthetic data for clinical trials, enabling various types of analyses. The package ensures consistency and robustness in handling different clinical trial datasets and generative models. Acting as a wrapper for several reliable generative modeling implementations, `pysdg` includes two main modules: `synth` and `privacy`.

### Documentation

Comprehensive documentation for the latest version of `pysdg` is available at [pysdg documentation](https://cheo-ehil.github.io/pysdg-releases/latest/index.html). For documentation related to specific versions, please visit [pysdg releases](https://cheo-ehil.github.io/pysdg-releases/).

### Note on Release Versions

The latest release of `pysdg` is a stable version and does not include a "b" in its release number, indicating it is not a beta release.

### Installation

You can install the package by using the appropriate release wheel file available in this repository. First, set up the virtual environment as detailed in the documentation. After downloading the wheel file, you can install it using pip. For example, to install `pysdg` v2.3.0, run:

```bash
pip install pysdg-2.3.0-py3-none-any.whl
```

Alternatively, you can download the relevant Docker image from [pysdg in Jupyter](https://github.com/CHEO-EHIL/pysdg-releases/pkgs/container/pysdg%2Fehil-py-pysdg) for `Python` users and from [pysdg in RStudio](https://github.com/CHEO-EHIL/pysdg-releases/pkgs/container/pysdg%2Fehil-r-pysdg-sdgm) for `R` users.

To install and use the test Docker image, ensure Docker is installed on your machine. For example, to use the latest version of the `pysdg` library in a Jupyter notebook, follow these steps:

```bash
docker pull ghcr.io/cheo-ehil/pysdg/ehil-py-pysdg:latest
docker run -p 8888:8888 -v /your/local/directory:/home/jovyan/data --name your-pysdg-image-name ghcr.io/cheo-ehil/pysdg/ehil-py-pysdg:latest
```

After executing these commands, follow the provided link to access the container via your web browser. Next, you can copy the tutorial files from the repository to your mapped /your/local/directory to start exploring `pysdg`.

Please be aware that the tutorial files are created using the latest version.

You can also find an RStudio-based image in the same link to the packages.

For any inquiries or support, please open an issue in this repository.

<p align="center">
  <img alt="EHIL-CHEO Logos" src="images/ehil_cheo.png" width="600" style="margin-right: 40px;">
</p>
