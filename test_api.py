"""
Test script for Student Task & Reminder API
Tests all endpoints including authentication
"""

import requests
import json
from datetime import datetime, timedelta

BASE_URL = "http://localhost:8001"
TOKEN = None
USER_ID = None


def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def test_health_check():
    """Test 1: Health Check"""
    print_section("Test 1: Health Check - GET /api/health")
    response = requests.get(f"{BASE_URL}/api/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    print("✓ Health check passed")


def test_register():
    """Test 2: User Registration"""
    print_section("Test 2: Register User - POST /auth/register")
    user_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "password": "secure_password_123"
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 201
    global USER_ID
    USER_ID = response.json()["id"]
    print(f"✓ User registered successfully (ID: {USER_ID})")


def test_register_duplicate():
    """Test 3: Try to register duplicate user"""
    print_section("Test 3: Register Duplicate User - POST /auth/register")
    user_data = {
        "username": "john_doe",
        "email": "john2@example.com",
        "password": "another_password_123"
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 400
    print("✓ Duplicate user rejection working")


def test_login():
    """Test 4: User Login"""
    print_section("Test 4: User Login - POST /auth/login")
    login_data = {
        "username": "john_doe",
        "password": "secure_password_123"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    global TOKEN
    TOKEN = response.json()["access_token"]
    print(f"✓ Login successful. Token obtained")


def test_login_invalid():
    """Test 5: Invalid Login"""
    print_section("Test 5: Invalid Login - POST /auth/login")
    login_data = {
        "username": "john_doe",
        "password": "wrong_password"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 401
    print("✓ Invalid login rejection working")


def test_create_task():
    """Test 6: Create a Task"""
    print_section("Test 6: Create Task - POST /tasks")
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    due_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    task_data = {
        "title": "Finish REST API project",
        "description": "Build backend using FastAPI",
        "due_date": due_date
    }
    response = requests.post(f"{BASE_URL}/tasks/",
                             json=task_data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 201
    global TASK_ID
    TASK_ID = response.json()["id"]
    print(f"✓ Task created successfully (ID: {TASK_ID})")


def test_create_task_no_auth():
    """Test 7: Try to create task without authentication"""
    print_section("Test 7: Create Task Without Auth - POST /tasks")
    task_data = {
        "title": "Another task",
        "description": "Should fail",
        "due_date": "2026-02-01"
    }
    response = requests.post(f"{BASE_URL}/tasks/", json=task_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 401
    print("✓ Authentication requirement working")


def test_get_all_tasks():
    """Test 8: Get All Tasks"""
    print_section("Test 8: Get All Tasks - GET /tasks")
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    response = requests.get(f"{BASE_URL}/tasks/", headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert len(response.json()) > 0
    print(f"✓ Retrieved {len(response.json())} task(s)")


def test_get_single_task():
    """Test 9: Get Single Task"""
    print_section("Test 9: Get Single Task - GET /tasks/{id}")
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    response = requests.get(f"{BASE_URL}/tasks/{TASK_ID}", headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json()["id"] == TASK_ID
    print(f"✓ Retrieved task with ID: {TASK_ID}")


def test_get_nonexistent_task():
    """Test 10: Get Non-existent Task"""
    print_section("Test 10: Get Non-existent Task - GET /tasks/{id}")
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    response = requests.get(f"{BASE_URL}/tasks/99999", headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 404
    print("✓ 404 error handling working")


def test_update_task():
    """Test 11: Update Task"""
    print_section("Test 11: Update Task - PUT /tasks/{id}")
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    update_data = {
        "title": "Finish REST API project - UPDATED",
        "description": "Build backend using FastAPI - Extended deadline"
    }
    response = requests.put(
        f"{BASE_URL}/tasks/{TASK_ID}", json=update_data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json()["title"] == "Finish REST API project - UPDATED"
    print("✓ Task updated successfully")


def test_complete_task():
    """Test 12: Mark Task as Completed"""
    print_section("Test 12: Complete Task - PATCH /tasks/{id}/complete")
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    response = requests.patch(
        f"{BASE_URL}/tasks/{TASK_ID}/complete", headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json()["is_completed"] == True
    print("✓ Task marked as completed")


def test_delete_task():
    """Test 13: Delete Task"""
    print_section("Test 13: Delete Task - DELETE /tasks/{id}")
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    response = requests.delete(f"{BASE_URL}/tasks/{TASK_ID}", headers=headers)
    print(f"Status Code: {response.status_code}")
    assert response.status_code == 204
    print("✓ Task deleted successfully")


def test_verify_task_deleted():
    """Test 14: Verify Task is Deleted"""
    print_section("Test 14: Verify Deleted Task - GET /tasks/{id}")
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    response = requests.get(f"{BASE_URL}/tasks/{TASK_ID}", headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 404
    print("✓ Task deletion verified")


def run_all_tests():
    """Run all tests"""
    try:
        test_health_check()
        test_register()
        test_register_duplicate()
        test_login()
        test_login_invalid()
        test_create_task()
        test_create_task_no_auth()
        test_get_all_tasks()
        test_get_single_task()
        test_get_nonexistent_task()
        test_update_task()
        test_complete_task()
        test_delete_task()
        test_verify_task_deleted()

        print_section("✓ ALL TESTS PASSED!")
        print("\nAPI is working correctly and ready for deployment!\n")

    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
    except requests.exceptions.ConnectionError:
        print("\n✗ Could not connect to API. Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("  Student Task & Reminder API - Test Suite")
    print("="*60)
    run_all_tests()
