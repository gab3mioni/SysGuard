import docker

client = docker.DockerClient(base_url='tcp://host.docker.internal:2375')

def list_containers():
    """Lista os containers Docker em execução"""
    containers = client.containers.list()
    return [
        {"id": c.id, "name": c.name, "status": c.status}
        for c in containers
    ]