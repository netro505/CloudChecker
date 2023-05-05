import docker
import tarfile

class Stormpy_lib:
    def check_model(file_name):
        client = docker.from_env()
        container = client.containers.get("stormpy") #sjunges/stormpyter:uai22
        # print(container.attrs['Config']['Image'])
        # logs = container.logs().decode('utf-8')
        # print(logs)

        # Create a tar archive of the file to be copied
        tar = tarfile.open('stormpy-app.tar', mode='w')
        tar.add('./stormpy-test3.py')
        tar.add(file_name)
        tar.add('model.txt')
        tar.add('prop.txt')
        # tar.add('properties-MDP-AISHAH')
        tar.close()

        # Copy the file to the containeSSSSSSSSSr
        with open('stormpy-app.tar', 'rb') as f:
            data = f.read()
            client.api.put_archive("stormpy", '/opt/stormpy', data)

        result = container.exec_run(
            'python stormpy-test3.py')
        print(result.output.decode())
        return result.output.decode()