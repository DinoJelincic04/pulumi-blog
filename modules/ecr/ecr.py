import pulumi
import pulumi_aws as aws
import json
import pulumi_eks as eks
import base64

ecr = aws.ecr.Repository("blog-repo",
        image_scanning_configuration=aws.ecr.RepositoryImageScanningConfigurationArgs(
            scan_on_push=True,
        ),
        name= "blog-repo",
        image_tag_mutability="IMMUTABLE")


#repository = ecr.Repository("myrepository")

repository_policy = aws.ecr.RepositoryPolicy(
    "myrepositorypolicy",
    repository=ecr.id,
    policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "new policy",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:DescribeRepositories",
                "ecr:GetRepositoryPolicy",
                "ecr:ListImages",
                "ecr:DeleteRepository",
                "ecr:BatchDeleteImage",
                "ecr:SetRepositoryPolicy",
                "ecr:DeleteRepositoryPolicy",
            ]
        }]
    })
)

lifecycle_policy = aws.ecr.LifecyclePolicy(
    "mylifecyclepolicy",
    repository=ecr.id,
    policy=json.dumps({
        "rules": [{
            "rulePriority": 1,
            "description": "Expire images older than 14 days",
            "selection": {
                "tagStatus": "untagged",
                "countType": "sinceImagePushed",
                "countUnit": "days",
                "countNumber": 14
            },
            "action": {
                "type": "expire"
            }
        }]
    })
)

kubeconfig_data = eks_cluster.kubeconfig.apply(lambda kc: kc)