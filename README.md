This gym manager provides an booking management system to allow a gym to manage and maintain its members, classes and bookings data.


# Features

- Add new members and set membership level at premium or off peak
- Edit members' information
- Deactivate members' accounts if no longer in use
- Create and edit classes and sessions
- Add and remove members to and from class sessions - restrictions are in place to avoid members being double booked on to a class, multiple sessions of the same type being booked at the same time, members being booked on to classes that are not available to their membership type, deactive accounts being added to classes

# Getting started

To initialise the database, run `psql -d [database_name] -f db/gym_manager.sql` in the terminal. 

If desired, existing member data can then be added to the console file and saved to the database by running `python3 console.py` in the terminal.

The app can then be run on a user's local device using the `flask run` command in the terminal while in the root directory and accessed at http://localhost:5000/ - or http://127.0.0.1:5000/.

# Using the app

From any page on the app, the navbar can be used to navigate to:

- Classes:
    - View all class types in order to access or edit
    - Add a new class type
- Sessions:
    - View all sessions within each class type in order to access or edit
    - Add a new session
- Members:
    - View all members in order to access or edit
    - Add a new member

