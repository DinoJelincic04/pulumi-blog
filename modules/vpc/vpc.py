import pulumi
import pulumi_aws as aws

eks_vpc = aws.ec2.Vpc("eks-vpc",
        cidr_block="10.100.0.0/16",
        instance_tenancy="default",
        tags={
            "Name": "eks-vpc",
        })

eks_gw = aws.ec2.InternetGateway("eks-gw",
        vpc_id=eks_vpc.id,
        tags={
            "Name": "eks-gw",
        })

eks_subnet1 = aws.ec2.Subnet("public subnet az1",
            vpc_id=eks_vpc.id,
            availability_zone="eu-central-1a",
            map_public_ip_on_launch=True,
            cidr_block="10.100.1.0/24",
            tags={
                "Name": "Public subnet AZ1",
            }) 

eks_subnet2 = aws.ec2.Subnet("public subnet az2",
            vpc_id=eks_vpc.id,
            availability_zone="eu-central-1b",
            map_public_ip_on_launch=True,
            cidr_block="10.100.2.0/24",
            tags={
                "Name": "Public subnet AZ2",
            })

eks_route_table = aws.ec2.RouteTable("eks-route-table",
                vpc_id=eks_vpc.id,
                routes=[
                    aws.ec2.RouteTableRouteArgs(
                    cidr_block="0.0.0.0/0",
                    gateway_id=eks_gw.id,),
                ],
                tags={
                    "Name": "Public route table",
                })

eks_route_table_association1 = aws.ec2.RouteTableAssociation("eks-route-table-association1",
                            subnet_id=eks_subnet1.id,
                            route_table_id=eks_route_table.id)

eks_route_table_association2 = aws.ec2.RouteTableAssociation("eks-route-table-association2",
                            subnet_id=eks_subnet2.id,
                            route_table_id=eks_route_table.id)

pulumi.export("vpcID", eks_vpc.id)
pulumi.export("publicSubnet1", eks_subnet1.id)
pulumi.export("publicSubnet1", eks_subnet2.id)
pulumi.export("internetGW", eks_gw.id)