from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
def find_event(event_id):
    return next((event for event in events if str(event.id) == str(event_id)), None)

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the Event Management API!"}), 200

@app.route('/events', methods=['GET'])
def get_events():
    # Converts the list of Event objects into a list of dictionaries
    return jsonify([event.to_dict() for event in events]), 200



# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()

    # TODO: Task 3 - Implement the Loop and Process Each Element
    if not data or 'title' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing 'title' in request body"}), 400

    # TODO: Task 4 - Return and Handle Results
    new_id = events[-1].id + 1 if events else 1
    new_event = Event(id=new_id, title=data['title'])
    events.append(new_event)
    
    return jsonify(new_event.to_dict()), 201



# TODO: Task 1 - Define the Problem
def find_event(event_id):
    return next((event for event in events if str(event.id) == str(event_id)), None)

# Update the title of an existing event ( PATCH /events/<int:id> )
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    event = find_event(id)

    # TODO: Task 3 - Implement the Loop and Process Each Element
    if not event:
        return jsonify({"error": "Not Found", "message": f"Event with ID {id} does not exist"}), 404
        
    data = request.get_json()

    # TODO: Task 4 - Return and Handle Results
    if not data or 'title' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing 'title' in request body"}), 400
        
    event.title = data['title']
    return jsonify(event.to_dict()), 200



# TODO: Task 1 - Define the Problem
def find_event(event_id):
    return next((event for event in events if str(event.id) == str(event_id)), None)

# Remove an event from the list ( DELETE /events/<int:id> )
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    event = find_event(id)

    # TODO: Task 3 - Implement the Loop and Process Each Element
    if not event:
        return jsonify({"error": "Not Found", "message": f"Event with ID {id} does not exist"}), 404

    # TODO: Task 4 - Return and Handle Results
    events.remove(event)
    return '', 204

    

if __name__ == "__main__":
    app.run(debug=True)
