from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.client import User
from diagrams.aws.compute import EC2, EKS
from diagrams.aws.database import RDS
from diagrams.onprem.network import Internet
from diagrams.aws.engagement import SES
from diagrams.aws.network import ELB, CF, PublicSubnet, PrivateSubnet, VPC, APIGateway, VPCRouter, InternetGateway, Route53, RouteTable, NATGateway

name_diagram = "PROYECTO"
filename_diagram = "nombrearchivo"

graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

input = Edge(color="blue")
output = Edge(color="red", style="dashed")

with Diagram(name_diagram, filename=filename_diagram, show=False, graph_attr=graph_attr, direction = "BT"):
    user = User("User")
    internet = Internet("internet")
    with Cluster("AWS"):
        cf = CF("CloudFront")
        dns = Route53("DNS")
        ses = SES("EMAIL")
        igw = InternetGateway("internet")

        with Cluster("VPC"):
            #VPC("VPC")
            #VPCRouter("Route")
            with Cluster("AZ1"):
                with Cluster("Subnet Public"):
                    elb1 = ELB("Public Load Balancer")
                    #PublicSubnet("Public Subnet 1A")
                    nat1 = NATGateway("NAT")
                with Cluster("Subnet Private"):
                    #PrivateSubnet("Private Subnet 1B")
                    with Cluster("EKS Cluster"):
                        eks1 = EKS()
                with Cluster("Subnet Secure"):
                    #PrivateSubnet("Private Subnet 1C")
                    rds1 = RDS("Master")
            with Cluster("AZ2"):
                with Cluster("Subnet Public"):
                    elb2 = ELB("Public Load Balancer")
                    #PublicSubnet("Public Subnet 2A")
                    nat2 = NATGateway("NAT")
                with Cluster("Subnet Private"):
                    #PrivateSubnet("Private Subnet 2B")
                    with Cluster("EKS Cluster"):
                        eks2 = EKS()
                with Cluster("Subnet Secure"):
                    #PrivateSubnet("Private Subnet 2C")
                    rds2 = RDS("Slave")
            with Cluster("AZ3"):
                with Cluster("Subnet Public"):
                    elb3 = ELB("Public Load Balancer")
                    #PublicSubnet("Public Subnet 3A")
                    nat3 = NATGateway("NAT")
                with Cluster("Subnet Private"):
                    #PrivateSubnet("Private Subnet 3B")
                    with Cluster("EKS Cluster"):
                        eks3 = EKS()
                with Cluster("Subnet Secure"):
                    #PrivateSubnet("Private Subnet 3C")
                    rds3 = RDS("Slave")

    user >> Edge() << internet
    internet >> dns
    internet >> cf
    internet >> igw

    igw >> input >> elb1
    igw >> input >> elb2
    igw >> input >> elb3

    elb1 >> input >> eks1
    elb2 >> input >> eks2
    elb3 >> input >> eks3

    eks1 >> output >> nat1
    eks2 >> output >> nat2
    eks3 >> output >> nat3

    eks1 >> output >> ses
    eks2 >> output >> ses
    eks3 >> output >> ses
    
    ses >> user

    nat1 >> output >> igw
    nat2 >> output >> igw
    nat3 >> output >> igw

    eks1 >> rds1
    eks2 >> rds1
    eks3 >> rds1

    rds1 - rds2
    rds1 - rds3