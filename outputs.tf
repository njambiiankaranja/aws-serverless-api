output "api_base_url" {
  value       = "${aws_apigatewayv2_api.lambda_api.api_endpoint}/items"
  description = "Base URL for the serverless API endpoint"
}