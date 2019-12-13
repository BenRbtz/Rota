# Rota Generator
## About
This project is used to generate rota for specified days within a month.

## File Structure
Hexagonal architecture is used with the following naming conventions inside the `rota` catalogue:
* `domain` - responsible for generating data that would be inserted into the rota
* `adapters` - responsible for the frameworks, technologies, etc that displays the rota

## App
### How to run
1. Build the Docker image: `docker image build . -t rota`
2. Run Docker image: `docker container run -it --rm -v /tmp:/tmp rota -d Monday -m March -f /tmp/file.xlsm`
### Argument Options  
| Option | Description | required | default value | allow multiple values | Example |
|:------:|:-----------:|:--------:|:-------:|:---------------------:|:-------:|
|--day_names, -d  | Day names to create rota for                             | yes |  none          | yes | Tuesday |
|--month_name, -m | Name of month to create rota for                         | yes |  none          | no  | February |
|--year, -y       | Year for rota                                            | yes | $CURRENT_YEAR  | no  |   2019 |
|--file_name, -f  | Directory and file name to write the spreadsheet         | no  | $PWD/rota.xlsx | no  | /tmp/rota.xlsx |

