Após conferir se o formato definido no arquivo `logstash.conf` está igual ao que é encontrado no log
subir o docker-compose.yaml e abrir o kibana que vai estar sem autenticação


## Teste manual de configuração do logstash

O logstash pode ser testado sem utilizar o elasticsearch usando o comando

```sh 
    echo 'Dec 06 11:11:01 prp-cr01-le01-ne01 containerd[2190]: time="2024-12-06T11:11:01.389588604Z" level=info msg="starting signal loop" namespace=moby path=/run/containerd/io.containerd.runtime.v2.task/moby/792a393081a2cc998b91fcc959fc9bca9596ec364c56999a8be1f64a58e481ea pid=1232189' | \
        podman run --rm -i \
        -v $(pwd)/manual-logstash.conf:/usr/share/logstash/pipeline/logstash.conf:ro \
        docker.elastic.co/logstash/logstash:8.10.2
```



--- 


After making sure the format defined on the file `logstash.conf` is what's going to be found on the log file
do docker-compose up and open kibana, which will be without authentication


## Manually testing the logstash configuration

It's possible to test the logstash config sintax/definition without using elasticsearch using the bellow command and adjusting the log message


```sh 
    echo 'Dec 06 11:11:01 prp-cr01-le01-ne01 containerd[2190]: time="2024-12-06T11:11:01.389588604Z" level=info msg="starting signal loop" namespace=moby path=/run/containerd/io.containerd.runtime.v2.task/moby/792a393081a2cc998b91fcc959fc9bca9596ec364c56999a8be1f64a58e481ea pid=1232189' | \
        podman run --rm -i \
        -v $(pwd)/manual-logstash.conf:/usr/share/logstash/pipeline/logstash.conf:ro \
        docker.elastic.co/logstash/logstash:8.10.2
```
