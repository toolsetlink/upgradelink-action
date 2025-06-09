# test_integration.py
import pytest
import requests
from main import main, fetch_json, call_api
import sys
import os


# 标记为集成测试，可能需要单独运行
@pytest.mark.integration
def test_fetch_json_real():
    # 使用公共测试API进行真实请求测试
    result = fetch_json('https://github.com/toolsetlink/tauri-demo/releases/download/tauri-demo-v0.1.0/latest.json')
    assert isinstance(result, dict)
    assert 'notes' in result
    assert 'version' in result


@pytest.mark.integration
def test_call_api_real():
    # 准备测试数据
    test_data = {
            "version": "0.1.0",
            "notes": "See the assets to download this version and install.",
            "pub_date": "2025-05-29T08:44:05.705Z",
            "platforms": {
                "darwin-aarch64": {
                    "signature": "dW50cnVzdGVkIGNvbW1lbnQ6IHNpZ25hdHVyZSBmcm9tIHRhdXJpIHNlY3JldCBrZXkKUlVUd3p5Rmx5UFN3YUtsemxTWGJRT2JiaTQrbHdpKzRtV3EzQVNnUUU5R2xNYU45ZjhmL0ZqbStXRHZvcndIbUJBeXNDNThxNWVkazlTamRLWkVCakl5V0wvcGJ6eFJCSGdBPQp0cnVzdGVkIGNvbW1lbnQ6IHRpbWVzdGFtcDoxNzQ4NTA4MDQ3CWZpbGU6dGF1cmktZGVtby5hcHAudGFyLmd6Ci9BZFRlSDllWTJVYThmamg1b1JpRC9vYmFidXpYZWYvcEF3MGswL1MwK3krY0Q4RDZ6YWxKS3Y5d21jSldSSlBsY1NudEVUZVRuVXlVaWR2Q05oeUNRPT0K",
                    "url": "https://github.com/toolsetlink/tauri-demo/releases/download/tauri-demo-v0.1.0/tauri-demo_aarch64.app.tar.gz"
                },
                "darwin-x86_64": {
                    "signature": "dW50cnVzdGVkIGNvbW1lbnQ6IHNpZ25hdHVyZSBmcm9tIHRhdXJpIHNlY3JldCBrZXkKUlVUd3p5Rmx5UFN3YU81aXhhUU9mWVFaaE1JTDVya0FObWtlZy9vYi9NQzM4SmU2cTFvTGdkVWhXWktYNzdHUWVuYzNpNnZXWG5BUk5NaDhJOEw3YzZoT21OQXFDVS9qaXd3PQp0cnVzdGVkIGNvbW1lbnQ6IHRpbWVzdGFtcDoxNzQ4NTA4MDgxCWZpbGU6dGF1cmktZGVtby5hcHAudGFyLmd6CktvMTRKU29XbVBKTHcwOFdBZUNYYWZNYzVqcjRYZVpFQkZUejVyMDlMWWFWUGVlMzJidXhkVHhUN2tWSS9haDgwOGhoVVdacnNHanR2U2NMWVBNaERnPT0K",
                    "url": "https://github.com/toolsetlink/tauri-demo/releases/download/tauri-demo-v0.1.0/tauri-demo_x64.app.tar.gz"
                },
                "linux-x86_64": {
                    "signature": "dW50cnVzdGVkIGNvbW1lbnQ6IHNpZ25hdHVyZSBmcm9tIHRhdXJpIHNlY3JldCBrZXkKUlVUd3p5Rmx5UFN3YVA2OEVHaEJDZW1PVmU3UWpaa1g5YXViVGp3NUFqKzRzcDlBM2xzM0JhaW9qZkZvenRoYU1IYk1acWpHWXpGTFZaZTZrNHBoNklvamp4anhYeFVaTkFZPQp0cnVzdGVkIGNvbW1lbnQ6IHRpbWVzdGFtcDoxNzQ4NTA4MTk1CWZpbGU6dGF1cmktZGVtb18wLjEuMF9hbWQ2NC5BcHBJbWFnZQo4a21ERnpVbWFQYnJLOVZ4RDJZQnNWTkRrQXNycUU5Wm83TFlPSWF0aThoYm9sM2lDcUhreXorbERJdzVBaGxEV2o5OXZYazdEVGlyWjZaOHNsR2hEQT09Cg==",
                    "url": "https://github.com/toolsetlink/tauri-demo/releases/download/tauri-demo-v0.1.0/tauri-demo_0.1.0_amd64.AppImage"
                },
                "windows-x86_64": {
                    "signature": "dW50cnVzdGVkIGNvbW1lbnQ6IHNpZ25hdHVyZSBmcm9tIHRhdXJpIHNlY3JldCBrZXkKUlVUd3p5Rmx5UFN3YU9ianFnc3NUdy9lcS8rQWJGTm5wTlFvS2JmTHl6ZGp5MjdRamFZUkE1VkR2R0pVUVVEMnFIMEYyOE9xSy9tMGU0UitpK1ZqeGE3WExkNVNyRWlRcHdnPQp0cnVzdGVkIGNvbW1lbnQ6IHRpbWVzdGFtcDoxNzQ4NTA4MjQzCWZpbGU6dGF1cmktZGVtb18wLjEuMF94NjRfZW4tVVMubXNpCmpkaU54K2NFUEJFOWNKVUwzeWxVWmVLYm1TTjM5TGNRR3RBT09mM3JxQmYydVAxRGJrSzRJRWMyeEIrL1UxYWM2azRVcVhQZXVtay9FQVllZE54WkRBPT0K",
                    "url": "https://github.com/toolsetlink/tauri-demo/releases/download/tauri-demo-v0.1.0/tauri-demo_0.1.0_x64_en-US.msi"
                }
            }
        }

    # 调用真实API
    result = call_api( 'mui2W50H1j-OC4xD6PgQag',  'a0jtz0HUwL66r7gCGvbMKQ','github', test_data)

    # 验证响应
    assert result.status_code == 200
    print(f"实际API响应: {result.text}")
