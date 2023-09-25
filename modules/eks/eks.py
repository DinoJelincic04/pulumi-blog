import pulumi
import pulumi_aws as aws
import modules.vpc.vpc as vpc
import modules.iam.iam as iam

eks_cluster = aws.eks.Cluster("eks-cluster",
            role_arn=iam.eks_cluster_role.arn,
            vpc_config=aws.eks.ClusterVpcConfigArgs(
                subnet_ids=[
                    vpc.eks_subnet1.id,
                    vpc.eks_subnet2.id,
                ],
            ),
        tags={
            "Name": "eks-blog-cluster",
        },
        opts=pulumi.ResourceOptions(depends_on=[iam.eks_cluster_role, vpc.eks_vpc]))

eks_workers = aws.eks.NodeGroup("eks-workers",
            cluster_name=eks_cluster.name,
            node_role_arn=iam.ec2_node_role.arn,
            instance_types=["t2.medium"],
            node_group_name="eks-blog-workers",
            subnet_ids=[
                vpc.eks_subnet1.id,
                vpc.eks_subnet2.id,
            ],
            scaling_config=aws.eks.NodeGroupScalingConfigArgs(
                desired_size=1,
                max_size=2,
                min_size=1,
            ),
            update_config=aws.eks.NodeGroupUpdateConfigArgs(
                max_unavailable=1,
            ),
            opts=pulumi.ResourceOptions(depends_on=[iam.ec2_node_role, eks_cluster]))




