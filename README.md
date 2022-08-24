# first_selenium
This project is used to run the selenium UI tests cases for the web site [a link](https://github.com/user/repo/blob/branch/other_file.md).

## Installation

Use the package manager [pip](https://pip.pypa.ffio/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```

## Used technologies
- Python
- Selenium
- Allure

## How to run

* to tun the test cases and generate the reports use:
```bash
pytest --alluredir=<reports path>
```
* To generate the HTML report from the JSon file use:

```bash
allure serve Reports
```
