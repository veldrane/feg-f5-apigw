from diagrams import Cluster, Diagram, Node, Edge
from diagrams.onprem.network import Nginx
from diagrams.onprem.client import Client
from diagrams.onprem.dns import Coredns
from diagrams.programming.language import Java, Python
from diagrams.k8s.compute import Pod

graph_attr = {
	"fontsize": "20",
	"bgcolor": "transparent"
}

edge_attr = {
    "arrowhead": "dot"
}

# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("Service discovery with NGINX Plus", show=True, outformat="svg", graph_attr=graph_attr) as diag:
    diag.dot.renderer = "cairo"
    # definice uzlu

    with Cluster("Openshift"):
        dns = Coredns("KubeDNS")
        primary = Nginx("Pod")

        with Cluster("Headless SVC #1"):
            be1 = [Pod("Pod #1"),
                        Pod("Pod #2"),
                        ]
        with Cluster("Headless SVC #2"):
            be2 = [Pod("Pod #1"),
                        Pod("Pod #2"),
                        ]

        dns >> Edge(minlen="6",color="blue", xlabel="2) get list of pods", fontsize="18", fontname="Arial Bold") >> primary
        primary >> Edge(minlen="6",color="blue", xlabel="1) DNS srv request to kubedns", fontsize="18", fontname="Arial Bold") >> dns
        primary >> Edge(minlen="6", xlabel="3) Use POD network, skip kubeproxy", fontsize="18", fontname="Arial Bold") >> be1
        primary >> Edge(minlen="6") >> be2

                        
 
    # propojeni uzlu grafu orientovanymi hranami


