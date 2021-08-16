# ls_pyenv

list up the names of Python virtualenvs which are written in .python-version files

## Motivation

If you are using pyenv (pyenv-virtualenv) and have many Python projects,
it is difficult to figure out which project is using which virtualenv.

So, I created a simple command to solve this problem.

## Installation

clone this repository and

* `> make install`
    * If you want to install `ls_pyenv` at your Python environment directly
* `> make install-pipx`
    * If you want to install `ls_pyenv` using pipx

## Usage

```
> ls-pyenv --help
usage: ls-pyenv [-h] [-d DIRECTORY]

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        the directory you search .python-version files
                        recursively. default: "." (current working directory)
```

## Sample Output

```
> ls-pyenv
Search under the directory: .
jupyter (3):
  deeplearning_models_pytorch
  object_detection_metrics
  practical_application_ai
ls-pyenv-jaMYHStk-py3.9 (1):
  ls_pyenv
nlp (2):
  fasttext_binary_jawiki
  mecab_dictionary
tflite (1):
  object_detection_tflite
vino (1):
  yolo_various_framework
```
