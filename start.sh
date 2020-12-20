#!/bin/bash
# Diretorio e arquivo de log
set -e
LOGFILE=/home/ifnmg/www/bqm/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
# Numero de processo simultaneo, modifique de acordo com seu processador
NUM_WORKERS=3
# Usuario/Grupo que vai rodar o gunicorn
USER=ifnmg
#GROUP=root
# Endereço local que o gunicorn irá rodar
ADDRESS=127.0.0.1:8000
# Ativando ambiente virtual e executando o gunicorn para este projeto
source /home/ifnmg/envs/bqm/bin/activate
cd /home/ifnmg/www/bqm/
#test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn -w $NUM_WORKERS --bind=$ADDRESS --user=$USER --log-level=debug --log-file=$LOGFILE 2>>$LOGFILE bqm.wsgi:application
#exec python3 manage.py runserver 200.131.5.61:8000

