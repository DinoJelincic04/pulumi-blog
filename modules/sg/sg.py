import pulumi
import pulumi_aws as aws
import modules.vpc.vpc as vpc

eks_sg = aws.ec2.SecurityGroup("eks_sg",
        description="firewall rules for cluster network",
        vpc_id= vpc.eks_vpc.id,
ingress=[{
            "protocol": "tcp",
            "from_port": 22,
            "to_port": 22,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "tcp",
            "from_port": 443,
            "to_port": 443,
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ],
    egress=[
        {
            "protocol": "-1",
            "from_port": 0,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ],
    
    tags={
        "Name": "eks-security-firewall-rules",
    },
    opts=pulumi.ResourceOptions(depends_on=[vpc.eks_vpc, vpc.eks_subnet1, vpc.eks_subnet2]))