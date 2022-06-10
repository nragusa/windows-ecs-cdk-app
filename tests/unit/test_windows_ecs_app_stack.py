import aws_cdk as core
import aws_cdk.assertions as assertions

from windows_ecs_app.windows_ecs_app_stack import WindowsEcsAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in windows_ecs_app/windows_ecs_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = WindowsEcsAppStack(app, "windows-ecs-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
