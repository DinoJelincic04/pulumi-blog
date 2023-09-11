import pulumi
import json
import pulumi_aws as aws

#IAM role for master

master_iam = aws.iam.Role("master-iam",
            assume_role_policy=json.dumps({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "eks.amazonaws.com"
        },
        "Action" : "sts:AssumeRole"
      }
    ]
  }),
  tags={
      "Name": "Master-IAM-role",
  })

master_attach1 = aws.iam.RolePolicyAttachment("master-attach1",
    role=master_iam.name,
    policy_arn="arn:aws:iam::aws:policy/AmazonEKSClusterPolicy")

master_attach2 = aws.iam.RolePolicyAttachment("master-attach2",
    role=master_iam.name,
    policy_arn="arn:aws:iam::aws:policy/AmazonEKSServicePolicy")

master_attach3 = aws.iam.RolePolicyAttachment("master-attach3",
    role=master_iam.name,
    policy_arn="arn:aws:iam::aws:policy/AmazonEKSVPCResourceController")

worker_iam = aws.iam.Role("worker-iam",
            assume_role_policy=json.dumps({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "ec2.amazonaws.com"
        },
        "Action" : "sts:AssumeRole"
      }
    ]
  }),
  tags={
      "Name": "Worker-IAM-role",
  })

worker_autoscaller = aws.iam.Policy("autoscaller_iam",
                path="/",
                description="ed-eks-autoscaler-policy",
                policy=json.dumps({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Action" : [
          "autoscaling:DescribeAutoScalingGroups",
          "autoscaling:DescribeAutoScalingInstances",
          "autoscaling:DescribeTags",
          "autoscaling:DescribeLaunchConfigurations",
          "autoscaling:SetDesiredCapacity",
          "autoscaling:TerminateInstanceInAutoScalingGroup",
          "ec2:DescribeLaunchTemplateVersions"
        ],
        "Effect" : "Allow",
        "Resource" : "*",
      }
    ],
  }))

worker_attach1 = aws.iam.RolePolicyAttachment("worker-attach1",
    role=worker_iam.name,
    policy_arn="arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy")

worker_attach2 = aws.iam.RolePolicyAttachment("worker-attach2",
    role=worker_iam.name,
    policy_arn="arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy")

worker_attach3 = aws.iam.RolePolicyAttachment("worker-attach3",
    role=worker_iam.name,
    policy_arn="arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore")

worker_attach4 = aws.iam.RolePolicyAttachment("worker-attach4",
    role=worker_iam.name,
    policy_arn="arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly")

worker_attach5 = aws.iam.RolePolicyAttachment("worker-attach5",
    role=worker_iam.name,
    policy_arn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess")

worker_attach6 = aws.iam.RolePolicyAttachment("worker-attach6",
    role=worker_iam.name,
    policy_arn=worker_autoscaller.arn)