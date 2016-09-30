import boto3
import sys

prefix = sys.argv[1]
client = boto3.client('cloudwatch',region_name='us-west-1')

response = client.describe_alarms(
  AlarmNamePrefix = prefix,
  StateValue = 'INSUFFICIENT_DATA',
  )

alarms = response['MetricAlarms']
alarm_names = [alarm['AlarmName'] for alarm in alarms]

print alarm_names[0]

response1 = client.delete_alarms(
  AlarmNames = alarm_names
  )


