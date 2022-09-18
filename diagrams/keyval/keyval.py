from diagrams import Cluster, Diagram, Node, Edge
from diagrams.onprem.network import Nginx
from diagrams.onprem.client import Client
from diagrams.programming.language import Java, Python
from diagrams.k8s.compute import Pod
from diagrams.onprem.identity import Dex

graph_attr = {
	"fontsize": "20",
	"bgcolor": "transparent"
}

edge_attr = {
    "arrowhead": "dot"
}

# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("OIDC code flow and nginx plus key/val", show=True, outformat="svg", graph_attr=graph_attr) as diag:
    diag.dot.renderer = "cairo"
    # definice uzlu

    fe1 = Client("Destop FE")

    with Cluster("Openshift"):

        idp = Dex("IdP")

        with Cluster("Backend Service #1"):
            be1 = [Pod("Pod #1"),
                        Pod("Pod #2"),
                        Pod("Pod #3"),
                        Pod("Pod #4"),
                        ]
        
        with Cluster("Nginx Cluster"):
            primary = Nginx("Pod")
            secondary = Nginx("Pod")
            primary - Edge(color="red", style="dashed", label = "Replication", fontsize="18", fontname="Arial Bold") - secondary
            secondary >> Edge(minlen="6") >> be1


    primary << Edge(color="blue", label="5) Get access + refresh tokens", fontsize="18", fontname="Arial Bold") << idp
    primary >> Edge(color="blue", label="4) Code exchange",fontsize="18", fontname="Arial Bold") >> idp

    fe1 >> Edge(color="black", label = "1) send credentials", fontsize="18", fontname="Arial Bold") >> idp
    fe1 << Edge(color="black", label = "2) get temporary code", fontsize="18", fontname="Arial Bold") << idp
    fe1 >> Edge(color="black", label = "3) temporary code", fontsize="18", fontname="Arial Bold") >> primary
    fe1 << Edge(color="black", label = "6) get token cookie", fontsize="18", fontname="Arial Bold") << primary
    fe1 >> Edge(color="green", label = "7) send request with auth cookie", fontsize="18", fontname="Arial Bold") >> primary
                        
 
    # propojeni uzlu grafu orientovanymi hranami


