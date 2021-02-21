#!/bin/bash
ARGS="$(cat /dev/stdin)"
ansible-playbook $ARGS

# ENV_ARGS="${ENV_ARGS:-}"
#ARGS="$@"

# ANSIBLE_EXEC="$(type ansible-playbook | awk '{print $3}')"

# 1>&2 echo "Argumentos recebidos"
# 1>&2 echo "$ARGS"
# 1>&2 echo "$ENV_ARGS"
# echo "chamar"

# LOG_FILE="/tmp/exec_${RANDOM}"
# bash -c "$ANSIBLE_EXEC $ARGS > $LOG_FILE" > /dev/null 2> /dev/null

# echo "Chamado o comando do ansible"
# echo "$ANSIBLE_EXEC $ARGS"
# echo "$saida"
# cat $LOG_FILE
# exit 0