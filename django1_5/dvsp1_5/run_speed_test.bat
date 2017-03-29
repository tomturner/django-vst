goto postgresql

:sqlite
set DATABASE_TYPE=sqlite
del sqlite3.db
move sqlite1_5.prof sqlite1_5_old.prof
python manage.py syncdb --noinput
python manage.py run_speed_test
move django1_5.prof sqlite1_5.prof
snakeviz sqlite1_5.prof
goto end

:firebird
set DATABASE_TYPE=firebird
del firebird.fdb
pause
move firebird1_5.prof firebird1_5_old.prof
isql.exe -q -i fbc.sql
python manage.py syncdb --noinput
python manage.py run_speed_test
move django1_5.prof firebird1_5.prof
snakeviz firebird1_5.prof
goto end

:postgresql
set DATABASE_TYPE=postgresql
move postgresql1_5.prof postgresql1_5_old.prof

python manage.py syncdb --noinput
python manage.py run_speed_test
move django1_5.prof postgresql1_5.prof
snakeviz postgresql1_5.prof
goto end


:end

