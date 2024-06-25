import os
import requests
import discord
import json
import random
import ossaudiodev

from replit import db

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tech_keywords = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning",
    "Natural Language Processing",
    "Computer Vision",
    "Big Data",
    "Cloud Computing",
    "Blockchain",
    "Internet of Things (IoT)",
    "5G",
    "Cybersecurity",
    "Augmented Reality",
    "Virtual Reality",
    "Quantum Computing",
    "Edge Computing",
    "DevOps",
    "Microservices",
    "APIs",
    "Serverless Computing",
    "Data Science",
    "Data Analytics",
    "Robotics",
    "Autonomous Vehicles",
    "Smart Cities",
    "Digital Twins",
    "Fintech",
    "Healthtech",
    "Edtech",
    "E-commerce",
    "SaaS (Software as a Service)",
    "PaaS (Platform as a Service)",
    "IaaS (Infrastructure as a Service)",
    "Kubernetes",
    "Docker",
    "CI/CD (Continuous Integration/Continuous Deployment)",
    "Artificial General Intelligence (AGI)",
    "Neural Networks",
    "Reinforcement Learning",
    "Distributed Ledger Technology",
    "Smart Contracts",
    "Drones",
    "Wearable Technology",
    "3D Printing",
    "Biometrics",
    "Voice Recognition",
    "Speech Synthesis",
    "Chatbots",
    "Predictive Analytics",
    "Recommendation Systems",
    "Data Mining",
    "Hadoop",
    "Spark",
    "NoSQL Databases",
    "Graph Databases",
    "SQL",
    "Blockchain",
    "Cryptocurrencies",
    "NFTs (Non-Fungible Tokens)",
    "Digital Transformation",
    "Industry 4.0",
    "Automation",
    "RPA (Robotic Process Automation)",
    "DevSecOps",
    "AI Ethics",
    "Explainable AI",
    "Digital Marketing",
    "SEO (Search Engine Optimization)",
    "SEM (Search Engine Marketing)",
    "CRM (Customer Relationship Management)",
    "ERP (Enterprise Resource Planning)",
    "BYOD (Bring Your Own Device)",
    "BYOC (Bring Your Own Cloud)",
    "BYOA (Bring Your Own App)",
    "BYON (Bring Your Own Network)",
    "Virtualization",
    "Hyperconvergence",
    "Software-Defined Networking (SDN)",
    "Network Function Virtualization (NFV)",
    "Infrastructure as Code (IaC)",
    "Zero Trust Security",
    "Identity and Access Management (IAM)",
    "SIEM (Security Information and Event Management)",
    "Endpoint Security",
    "Unified Threat Management (UTM)",
    "Threat Intelligence",
    "Incident Response",
    "Disaster Recovery",
    "Business Continuity",
    "Penetration Testing",
    "Vulnerability Management",
    "Cyber Threat Hunting",
    "Malware Analysis",
    "Phishing",
    "Ransomware",
    "Data Encryption",
    "Public Key Infrastructure (PKI)",
    "Quantum Cryptography",
    "Homomorphic Encryption",
    "Synthetic Data",
    "Federated Learning",
    "Privacy-Preserving Computation",
    "Genomics",
    "Proteomics",
    "Bioinformatics",
    "Telemedicine",
    "Digital Health",
    "Smart Contracts",
    "Distributed Apps (DApps)"
]

tech_learning_links = [
    "https://www.coursera.org/learn/ai-for-everyone",
    "https://www.coursera.org/learn/machine-learning",
    "https://www.coursera.org/specializations/deep-learning",
    "https://www.coursera.org/learn/natural-language-processing",
    "https://www.coursera.org/learn/computer-vision-basics",
    "https://www.edx.org/professional-certificate/big-data",
    "https://www.coursera.org/specializations/cloud-computing",
    "https://www.coursera.org/specializations/blockchain",
    "https://www.coursera.org/specializations/internet-of-things",
    "https://www.edx.org/course/introducing-5g",
    "https://www.coursera.org/specializations/it-security",
    "https://www.coursera.org/learn/ar",
    "https://www.coursera.org/specializations/virtual-reality",
    "https://www.edx.org/course/quantum-computing",
    "https://www.coursera.org/learn/edge-computing",
    "https://www.coursera.org/specializations/devops",
    "https://www.coursera.org/specializations/microservices",
    "https://www.coursera.org/learn/api",
    "https://www.coursera.org/learn/serverless-computing",
    "https://www.coursera.org/specializations/jhu-data-science",
    "https://www.coursera.org/specializations/business-analytics",
    "https://www.coursera.org/specializations/robotics",
    "https://www.coursera.org/learn/self-driving-cars",
    "https://www.coursera.org/learn/smart-cities",
    "https://www.coursera.org/learn/digital-twins",
    "https://www.coursera.org/specializations/fintech",
    "https://www.coursera.org/learn/healthcare-innovation",
    "https://www.coursera.org/learn/edtech",
    "https://www.coursera.org/learn/ecommerce",
    "https://www.coursera.org/learn/saas",
    "https://www.coursera.org/learn/paas",
    "https://www.coursera.org/learn/iaas",
    "https://www.coursera.org/learn/kubernetes",
    "https://www.coursera.org/learn/docker",
    "https://www.coursera.org/learn/ci-cd",
    "https://www.udacity.com/course/intro-to-artificial-intelligence--cs271",
    "https://www.coursera.org/learn/neural-networks-deep-learning",
    "https://www.coursera.org/specializations/reinforcement-learning",
    "https://www.coursera.org/learn/distributed-ledger-technology",
    "https://www.coursera.org/learn/smart-contracts",
    "https://www.coursera.org/learn/drones",
    "https://www.coursera.org/learn/wearable-technologies",
    "https://www.coursera.org/learn/3d-printing",
    "https://www.coursera.org/learn/biometrics",
    "https://www.coursera.org/learn/voice-recognition",
    "https://www.coursera.org/learn/speech-synthesis",
    "https://www.coursera.org/learn/chatbots",
    "https://www.coursera.org/specializations/predictive-analytics",
    "https://www.coursera.org/learn/recommender-systems",
    "https://www.coursera.org/specializations/data-mining",
    "https://www.coursera.org/learn/hadoop",
    "https://www.coursera.org/learn/apache-spark",
    "https://www.coursera.org/learn/nosql-databases",
    "https://www.coursera.org/learn/graph-databases",
    "https://www.coursera.org/learn/sql",
    "https://www.coursera.org/specializations/blockchain",
    "https://www.coursera.org/learn/cryptocurrency",
    "https://www.coursera.org/learn/nft",
    "https://www.coursera.org/specializations/digital-transformation",
    "https://www.coursera.org/learn/industry-4-0",
    "https://www.coursera.org/learn/automation",
    "https://www.coursera.org/specializations/rpa",
    "https://www.coursera.org/learn/devsecops",
    "https://www.coursera.org/learn/ai-ethics",
    "https://www.coursera.org/learn/explainable-ai",
    "https://www.coursera.org/specializations/digital-marketing",
    "https://www.coursera.org/learn/seo",
    "https://www.coursera.org/learn/sem",
    "https://www.coursera.org/learn/crm",
    "https://www.coursera.org/learn/erp",
    "https://www.coursera.org/learn/byod-security",
    "https://www.coursera.org/learn/cloud-computing",
    "https://www.coursera.org/learn/mobile-app-development",
    "https://www.coursera.org/learn/network-security",
]

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello! Welcome')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    msg = message.content

    if any(word in msg for word in tech_keywords):
        await message.channel.send(random.choice(tech_learning_links))

try:
    token = os.getenv("TOKEN") or ""
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")
    client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests.")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e
