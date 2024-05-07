# Installation Options
## Installation From Pip

1. Create a virutalenv: `python -m venv .venv`
2. Activate the virtualenv: `source .venv/bin/activate`
3. Install modelbench and huggingface plugins: `pip install modelbench modelgauge-huggingface`
4. Install this package: `pip install -e .`
5. Ensure your configuration file has appropriate keys: https://github.com/mlcommons/modelbench?tab=readme-ov-file#trying-it-out
6. Run modelbench with new SUT: `modelbench benchmark -s openai-gpt -m 10`

## Copy into ModelBench Repo

1. Clone ModelBench: `git clone git@github.com:mlcommons/modelbench.git`
2. Install ModelBench: https://github.com/mlcommons/modelbench?tab=readme-ov-file#installation
3. Install huggingface plugin: `poetry add modelgauge-huggingface`
4. Ensure your configuration file has appropriate keys: https://github.com/mlcommons/modelbench?tab=readme-ov-file#trying-it-out
5. Copy this repo's `modelgauge` directory into ModelBench's `src` directory.
6. Run ModelBench from the `modelbench` repository: `poetry run modelbench benchmark -s openai-gpt -m 10`

## Install into ModelBench Repo
1. Clone ModelBench: `git clone git@github.com:mlcommons/modelbench.git`
2. Install ModelBench: https://github.com/mlcommons/modelbench?tab=readme-ov-file#installation
3. Install huggingface plugin and this package: `poetry add git+ssh://git@github.com:dhosterman/simplest-modelbench-sut.git modelgauge-huggingface`
4. Ensure your configuration file has appropriate keys: https://github.com/mlcommons/modelbench?tab=readme-ov-file#trying-it-out
5. Run ModelBench from the `modelbench` repository: `poetry run modelbench benchmark -s openai-gpt -m 10`