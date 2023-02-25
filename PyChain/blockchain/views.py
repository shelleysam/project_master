from django.shortcuts import render
import datetime
import hashlib
import json
from uuid import uuid4,uuid1
import socket
import requests
from urllib.parse import urlparse
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt #New
from rest_framework.parsers import JSONParser


class Blockchain:

    def __init__(self):
        self.chain = []
        self.transactions = [] 
        self.applications = [] #new
        self.create_block(nonce = 1, previous_hash = '0', private_key='1')
        self.nodes = set() 

    def create_block(self, nonce, previous_hash, private_key):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'nonce': nonce,
                 'private_key':private_key,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions, 
                 'applications': self.applications
                }
        self.transactions = []
        self.applications = [] #new
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]
    
    def private_key(self,index):
        pk=hashlib.sha256(str(index**2).encode()).hexdigest()
        return pk

    def proof_of_work(self, previous_nonce):
        new_nonce = 1
        check_nonce = False
        while check_nonce is False:
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        return new_nonce

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_nonce = previous_block['nonce']
            nonce = block['nonce']
            hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

    def add_transaction(self, sender, receiver, DATA, time): 
        self.transactions.append({'sender': sender,
                                  'receiver': receiver,
                                  'DATA': DATA,
                                  'time': str(datetime.datetime.now())})
        previous_block = self.get_last_block()
        return previous_block['index'] + 1
    
    
    def add_application( self, index, app_uid,time):#NEW
        self.applications.append({'index': index,
                                  'app_uid': app_uid,
                                  'time':str(datetime.datetime.now())})
        previous_block = self.get_last_block()
        return previous_block['index'] + 1

    def add_application1( self, index, app_uid, appname, time):#NEW
        return blockchain.chain[int(index)-1]

    def get_block(self, data):
        data1= (list(data.values()))
        index=int(data1[0])-1
        return blockchain.chain[index]

    def add_node(self, address): #New
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)


    def replace_chain(self): #New
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False


# Creating our Blockchain
blockchain = Blockchain()
# Creating an address for the node running our server
node_address = str(uuid4()).replace('-', '') #New
root_node = 'e36f0158f0aed45b3bc755dc52ed4560d' #New

@csrf_exempt
def mine_block(request):
    if request.method == 'POST':
        data=JSONParser().parse(request)
        previous_block = blockchain.get_last_block()
        previous_nonce = previous_block['nonce']
        nonce = blockchain.proof_of_work(previous_nonce)
        private_key=blockchain.private_key(nonce)
        previous_hash = blockchain.hash(previous_block)
        blockchain.add_transaction(sender = root_node, receiver = node_address, DATA=data, time=str(datetime.datetime.now()))
        blockchain.add_application(index= '0',app_uid= '0',time=str(datetime.datetime.now()))
        block = blockchain.create_block(nonce, previous_hash, private_key)
        response = {'message': 'Congratulations, you just mined a block!',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'nonce': block['nonce'],
                    'private_key': block['private_key'],
                    'previous_hash': block['previous_hash'],
                    'transactions': block['transactions'],
                    'applications': block['applications']}#new
    return JsonResponse(response)

# Getting the full Blockchain
def get_chain(request):
    if request.method == 'GET':
        response = {'chain': blockchain.chain,
                    'length': len(blockchain.chain)}
    return JsonResponse(response)

@csrf_exempt
#get one block
def get_details(request):
    if request.method =='GET':
        index = json.loads(request.body)
        block = blockchain.get_block(index)
        response={'details': block['transactions']}
    return JsonResponse(response)

#get one app of block
def get_app(request):
    if request.method =='GET':
        index = json.loads(request.body)
        block = blockchain.get_block(index)
        response={'details': block['applications']}
    return JsonResponse(response)

# Checking if the Blockchain is valid
def is_valid(request):
    if request.method == 'GET':
        is_valid = blockchain.is_chain_valid(blockchain.chain)
        if is_valid:
            response = {'message': 'All good. The Blockchain is valid.'}
        else:
            response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return JsonResponse(response)

# Adding a new transaction to the Blockchain
@csrf_exempt
def add_transaction(request): #New
    if request.method == 'POST':
        received_json = json.loads(request.body)
        transaction_keys = ['sender', 'receiver', 'DATA','time']
        if not all(key in received_json for key in transaction_keys):
            return 'Some elements of the transaction are missing', HttpResponse(status=400)
        index = blockchain.add_transaction(received_json['sender'], received_json['receiver'], received_json['DATA'],received_json['time'])
        response = {'message': f'This transaction will be added to Block {index}'}
    return JsonResponse(response)

@csrf_exempt
def add_app(request): #New
    if request.method == 'POST':
        received_json = json.loads(request.body)
        index = received_json['index']
        app=blockchain.add_application1(received_json['index'],received_json['appname'],
                                        received_json['uid'],received_json['time'])
        app['applications'].append({'index':len(app['applications']),'appname':received_json['appname'],'uid':received_json['uid']})
    return JsonResponse("done",safe=False)

# Connecting new nodes
@csrf_exempt
def connect_node(request): #New
    if request.method == 'POST':
        received_json = json.loads(request.body)
        nodes = received_json.get('nodes')
        if nodes is None:
            return "No node", HttpResponse(status=400)
        for node in nodes:
            blockchain.add_node(node)
        response = {'message': 'All the nodes are now connected. The Sudocoin Blockchain now contains the following nodes:',
                    'total_nodes': list(blockchain.nodes)}
    return JsonResponse(response)

# Replacing the chain by the longest chain if needed
@csrf_exempt
def replace_chain(request): #New
    if request.method == 'GET':
        is_chain_replaced = blockchain.replace_chain()
        if is_chain_replaced:
            response = {'message': 'The nodes had different chains so the chain was replaced by the longest one.',
                        'new_chain': blockchain.chain}
        else:
            response = {'message': 'All good. The chain is the largest one.',
                        'actual_chain': blockchain.chain}
    return JsonResponse(response)