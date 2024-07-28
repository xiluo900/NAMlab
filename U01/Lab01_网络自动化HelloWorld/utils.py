import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# 这里替换为你的InfluxDB信息
token = "YhQTsQScbFSEJvOeiChL-ukzoP2Ds0WBCm-A2sNQrLdg3cBbVcRfjtljs4_VH5NI8IKc7K83t8jlgvyAf4Z4FA=="
org = "C_A"
bucket = "monitor"
influx_server = "http://8.138.90.155:8086"

class DataWriter:
    def __init__(self):
        client = influxdb_client.InfluxDBClient(url=influx_server, token=token, org=org)
        self.api_writer = client.write_api(write_options=SYNCHRONOUS)

    def write_ts_data(self, pname, field_tup):
        data_point = influxdb_client.Point(pname).field(field_tup[0], field_tup[1])
        self.api_writer.write(bucket=bucket, org=org, record=data_point)