import pulumi
import pulumi_aws as aws

ecr = aws.ecr.Repository("blog-repo",
        image_scanning_configuration=aws.ecr.RepositoryImageScanningConfigurationArgs(
            scan_on_push=True,
        ),
        image_tag_mutability="IMMUTABLE")
