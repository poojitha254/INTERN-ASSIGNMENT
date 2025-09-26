from locust import HttpUser, task, between

class ReqresUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def list_users(self):
        self.client.get("/api/users?page=2")

    @task
    def single_user(self):
        self.client.get("/api/users/2")
