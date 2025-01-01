fake_users_db = {
    "user": {
        "username": "user",
        "role": "user",
        "name": "John Doe",
        "email": "john@example.com",
        "hashed_password": "$2b$12$q0SxFO0WEfv.nGcCPRDr5ul6bDiGvNCKihCs2S5dKUqm4sbqer39y",
    },
    "admin": {
        "username": "admin",
        "role": "admin",
        "name": "Admin Master",
        "email": "admin@example.com",
        "hashed_password": "$2b$12$XjOtNabUwdNevZbUdwXr9OZGnnGXFg9s.T6Z3V4iJLZEOsPhZpqAa",
    },
}


fake_purchases_db = {
    "user": [
        {"id": 1, "item": "Laptop", "price": 2500},
        {"id": 2, "item": "Smartphone", "price": 1200},
    ]
}

fake_reports_db = {
    "admin": [
        {"id": 1, "title": "Monthly Sales", "status": "Completed"},
        {"id": 2, "title": "User Activity", "status": "Pending"},
    ]
}
