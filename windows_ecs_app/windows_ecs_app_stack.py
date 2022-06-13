from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns
)
from constructs import Construct


class WindowsEcsAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # default is all AZs in region
        vpc = ec2.Vpc(self, 'ContainersVPC', max_azs=3)

        cluster = ecs.Cluster(self,
                              'WindowsAppCluster',
                              vpc=vpc)

        windows_task = ecs.FargateTaskDefinition(
            self,
            'WindowsAppTask',
            cpu=1024,
            memory_limit_mib=2048,
            runtime_platform=ecs.RuntimePlatform(
                cpu_architecture=ecs.CpuArchitecture.X86_64,
                operating_system_family=ecs.OperatingSystemFamily.WINDOWS_SERVER_2019_CORE
            )
        )
        windows_task.add_container(
            'WindowsAppContainer',
            image=ecs.ContainerImage.from_registry(
                'mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019'
            ),
            logging=ecs.LogDrivers.aws_logs(
                stream_prefix='WindowsAppService'
            ),
            port_mappings=[
                ecs.PortMapping(
                    container_port=80,
                    protocol=ecs.Protocol.TCP
                )
            ]
        )
        ecs_patterns.ApplicationLoadBalancedFargateService(self,
                                                           'WindowsAppService',
                                                           cluster=cluster,
                                                           desired_count=2,
                                                           task_definition=windows_task,
                                                           min_healthy_percent=100,
                                                           public_load_balancer=True
                                                           )
