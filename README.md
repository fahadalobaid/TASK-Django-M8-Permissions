Protect our views 🫣

## Steps

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Django-M8-Permissions).
2. Create a virtual environment.
3. Install the packages using `pip install -r requirements/dev.lock`.
4. Adjust the permissions of the `BookingsList` and `BookFlight` so that only logged in users can access this view.
5. Adjust the permissions of the `BookingDetails`, `UpdateBooking` and `CancelBooking` so that only an owner of the booking or staff can access the view.
6. Adjust the permissions of the `UpdateBooking` and `CancelBooking` so that the booking cannot be canceled or modified unless it's more than 3 days away.
7. Test your modified APIs on `Postman`.
8. Push your code.
