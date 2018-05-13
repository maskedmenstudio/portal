import yaml
import queue

from kubernetes import client, config

class PoolManager:

    __instance = None
    __yaml_location = "deploy_game.yaml"

    def __init__(self, max_players):
        if PoolManager.__instance != None:
            return PoolManager.__instance

        self.max_players = max_players
        self.queue = queue.Queue(maxsize=self.max_players)
        self.yaml_deployment = self.getYaml()

    def getYaml(self):
        with open('/deploy.yaml', 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                return exc

    def addPlayer(self, player):
        self.queue.put(player)
        if self.queue.full:
            self.spawnContainer(123)
    
    def spawnContainer(self, port):
        file=open("/var/run/secrets/kubernetes.io/serviceaccount/namespace","r")
        namespace=file.readline()
        file.close()
        
        config.load_incluster_config()
        v1 = client.CoreV1Api()
        v1.create_namespaced_pod(namespace, self.yaml_deployment)

    def portForward(self, port):
        return
