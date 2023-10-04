import pulumi
import pulumi_aws as aws
import json

eks_cluster_role = aws.iam.Role("eks-iam-role",
            assume_role_policy=json.dumps({
                'Version': '2012-10-17',
                'Statement': [
                    {
                        'Action': 'sts:AssumeRole',
                        'Principal': {
                            'Service': 'eks.amazonaws.com'
                        },
                        'Effect': 'Allow',
                        'Sid':''     
                    }
                            ],


            }),
    )

aws.iam.RolePolicyAttachment(
    'eks-cluster-policy-attachment',
    role=eks_cluster_role.id,
    policy_arn='arn:aws:iam::aws:policy/AmazonEKSClusterPolicy',
)

ec2_node_role = aws.iam.Role("ec2-node-iam-role",
                         assume_role_policy=json.dumps({
                             'Version': '2012-10-17',
                             'Statement': [
                                 {
                                     'Action': 'sts:AssumeRole',
                                     'Principal': {
                                         'Service': 'ec2.amazonaws.com'
                                     },
                                     'Effect': 'Allow',
                                     'Sid': ''
                                 }
                             ],
                         }),
    )
aws.iam.RolePolicyAttachment("eks-workernode-policy-attachment",
                         role=ec2_node_role.id,
                         policy_arn='arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy',)

aws.iam.RolePolicyAttachment("eks-cni-policy-attachment",
                         role=ec2_node_role.id,
                         policy_arn='arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy',)

aws.iam.RolePolicyAttachment("eks-container-policy-attachment",
                         role=ec2_node_role.id,
                         policy_arn='arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly',)