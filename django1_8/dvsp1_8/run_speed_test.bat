goto firebird

:sqlite
set DATABASE_TYPE=sqlite
del sqlite3.db
pause
move sqlite1_8.prof sqlite1_8_old.prof
python manage.py syncdb --noinput
python manage.py run_speed_test
move django1_8.prof sqlite1_8.prof
snakeviz sqlite1_8.prof
goto end

:firebird
set DATABASE_TYPE=firebird
del firebird.fdb
pause
move firebird1_8.prof firebird1_8_old.prof
isql.exe -q -i fbc.sql
python manage.py syncdb --noinput
python manage.py run_speed_test
move django1_8.prof firebird1_8.prof
snakeviz firebird1_8.prof
goto end

:postgresql
set DATABASE_TYPE=postgresql
move postgresql1_8.prof postgresql1_8_old.prof

python manage.py syncdb --noinput
python manage.py run_speed_test
move django1_8.prof postgresql1_8.prof
snakeviz postgresql1_8.prof
goto end


:end

