# How to run application (via src)
pip install -r requirements/src.txt
pip install -e .
python app.py -d  Monday Thursday -m March

# How to run app (via Docker)
docker container run -it --rm -v /tmp:/tmp rota -d Monday -m March -f /tmp/file.xlsm


# Application argument options
-f or --file_name  to set the output spreadsheet name (optional)

-y or --year       to set rota year (optional)

-m or --month_name to set rota month (required)

-d or --day_names  to set rota days of week (required)

