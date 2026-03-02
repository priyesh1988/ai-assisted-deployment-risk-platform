
provider "aws" {
  region = "us-east-1"
}

resource "aws_eks_cluster" "ai_risk_cluster" {
  name     = "ai-risk-cluster"
  role_arn = "arn:aws:iam::123456789012:role/eks-cluster-role"
}
