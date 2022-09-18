from diagrams import Cluster, Diagram, Node, Edge
from diagrams.oci.devops import APIGateway
from diagrams.generic.os import IOS, Android, Windows, LinuxGeneral
from diagrams.generic.device import Mobile, Tablet
from diagrams.programming.language import Go, Nodejs, Java, Python

graph_attr = {
	"fontsize": "20",
	"bgcolor": "transparent"
}

edge_attr = {
    "arrowhead": "dot"
}

# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("Api Gateway example", show=True, outformat="svg", graph_attr=graph_attr) as diag:
    diag.dot.renderer = "cairo"
    # definice uzlu

    fe1 = Mobile("Mobile FE")
    fe2 = Tablet("Mobile FE")
    fe3 = LinuxGeneral("Destop FE")
    fe4 = IOS("Destop FE")

    with Cluster("Company"):

        with Cluster("Backend microservices"):
            bes1 = [Go("Microservice"),
                        Go("Microservice"),
                        Java("Microservice"),
                        Java("Microservice")
                        ]
        
        apigw1 = APIGateway("API Gateway")
 
    # propojeni uzlu grafu orientovanymi hranami
    fe1 >> Edge(minlen="6", label="REST") >> apigw1
    fe2 >> Edge(minlen="6", label="REST") >> apigw1
    fe3 >> Edge(minlen="6", label="REST") >> apigw1
    fe4 >> Edge(minlen="6", label="REST") >> apigw1
    apigw1 >> Edge(minlen="6") >> bes1

