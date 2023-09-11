import pulumi
#import pulumi_kubernetes as k8s
import modules.eks.eks as eks



#eks_provider = k8s.Provider("eks-provider", kubeconfig=eks.eks_cluster.kubeconfig_json)