import pulumi
import modules.vpc.vpc as vpc
import modules.sg.sg as sg
import modules.iam.iam as iam
import modules.eks.eks as eks
import modules.ecr.ecr as ecr
pulumi.export('vpcCIDR', vpc.eks_vpc.cidr_block)
pulumi.export("securityGroupID", sg.eks_sg.id)
pulumi.export("masterARN", iam.master_iam.arn)
pulumi.export("workerARN", iam.worker_iam.arn)
pulumi.export("clusterEndpoint", eks.eks_cluster.endpoint)
pulumi.export("kubeconfigCA", eks.eks_cluster.certificate_authority)
pulumi.export("repo-url", ecr.ecr.repository_url)
