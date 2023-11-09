from diagrams import Diagram, Cluster
from diagrams.aws.compute import EKS
from diagrams.aws.network import VPC, ElbNetworkLoadBalancer
from diagrams.aws.network import PrivateSubnet
from diagrams.aws.network import PublicSubnet
from diagrams.aws.compute import Compute
from diagrams.k8s.compute import Pod

with Diagram("Architectural Diagram", show=False, direction="TB") as dg:
    source = EKS("Demo(EKS Control Plane)")

    with Cluster("Main(VPC)"):
        with Cluster("Availability Zone1(ap-south-1a)"):
            with Cluster("Private subnet1(private-ap-south-1a)"):
                pr_sub1_nodes = [Compute ("private-node1")]
                pr_sub1_pods = [Pod ("hello1"),
                        Pod ("hello2")]
                 
            with Cluster("Public subnet1(public-ap-south-1a)"):
                pu_sub1_nodes = [Compute("no node")]

        with Cluster("Availability Zone2(ap-south-1b)"):
            with Cluster("Private subnet2(private-ap-south-1b)"):
                pr_sub2_nodes = [Compute ("private-node2")]
                pr_sub2_pods = [Pod ("hello3"),
                        Pod ("hello4")]
                
            with Cluster("Public subnet2(public-ap-south-1b)"):
                pu_sub2_nodes = [Compute ("no node")]
        
        with Cluster("Availability Zone(ap-south-1aorb)"):
            with Cluster("Auto scaling group"):
                with Cluster("Private subnet"):
                    pr_sub3_nodes = [Compute ("private-node3")]
                    pr_sub3_pods = [Pod ("hello5"),
                            Pod ("hello6")]
                
                with Cluster("Public subnet"):
                    pu_sub3_nodes = [Compute ("no node")]
        
        
            
    source >> pr_sub1_nodes
    source >> pr_sub2_nodes
    source >> pr_sub3_nodes
    
    
dg


