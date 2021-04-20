Criar uma tarefa com cada host
    for i in {1..5}; do ./new_task.py `echo '{"target": "lab_clients_'$i'.lab_default"}'`; done

    