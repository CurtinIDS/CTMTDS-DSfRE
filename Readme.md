# DSfRE Training working June 2025
A repo for hosting training material for the DSfRE workshop


## Workshop Organisers
- Aloke Phatak
- Leigh Tyers
- Torrance Hodgson


## Attendees
1. In Seeq, click the git icon on the left hand side.
2. Click "Clone Repo"
3. Copy paste the url for this repo into the text box
4. Hit ok

## Developer Notes
Below are notes for developing these resources
### Installation Steps
1. Install Quarto by following Step 1 of the instructions [here](https://quarto.org/docs/get-started/)
2. Install python, for example via [miniforge](https://github.com/conda-forge/miniforge)
3. Create a venv (via `venv` or `mamba`) and install the necessary dependencies:
```sh
python -m pip install requirements.txt
```


### Building QMD Files
In a terminal, navigate to the directory you wish to build, activate your environment and run:
```sh
quarto preview <path_to_qmd_file.qmd> --no-browser
```

### Rendering all slides
1. Install the rsvg-convert
- macOS: `brew install librsvg`
- Ubuntu `sudo apt install librsvg2-bin`
2. Edit the script with preferred variables `output_format`(`pdf` or `html`) and `output_folder`
3. Run the script with your shell of choice
4. Local file paths for output are relative to the script directory

