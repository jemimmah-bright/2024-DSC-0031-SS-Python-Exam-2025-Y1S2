
from flask import Flask, request, jsonify
app = Flask(__name__)

programs = {}
courses = {}
students = {}

# for the ids to automatically increase
program_id = 1
course_id = 1
student_id = 1

# Our End points

# creating a new program
@app.route('/programs', methods = ['POST'])
def create_program():
    data= request.json
    pid=program_id_counter
    programs[pid] = {"id":pid,"name" :data["name"],"duration":data.get("duration")}
    program_id_counter +=1
    return jsonify(programs[pid]), 201
    

# creating a new course
@app.route('/courses', methods =['POST'])
def create_courses():
    data = request.json
    cid =course_id_counter
    if data["program_id"] not in programs:
        return jsonify ({"error": "program not foung"})  , 404
    courses [cid]= {"id":cid, "name": date ["name"], "program_id": data ["program_id"]}
    course_id_counter +=1
    return jsonify(courses[cid]), 201
    

# creating a new student
@app.route ('students', methods = ['POST'])
def create_student():
    data = request.json
    sid = student_id_counter
    if data ["program_id"] not in programs:
        return jsonify({"error": "program not found"}), 404
    


    students [sid]= {

        "id": sid,
        "name": data ["name"],
        "email": data["email"],
        "program_id":data["program_id"],
        "enrolled_courses": data.get("enrolled courses", [])
    }

    student_id_counter +=1
    return jsonify(students[sid]), 201
    

#getting all students
@app.route('/students', methods = ['GET'])
def get_students():
    return jsonify(list (students.values()))

# deleting a student

@app.route('/student/<int:sid>', methods = ['DELETE'])
def delete_student(sid):
    if sid in students:
        del students[sid]
        return jsonify({"message": " student Deleted sucessfully"}), 200
    else:
        return jsonify({"error":"student not founf"}), 404

# updating a program
@app.route('/programs/<int:pid>', methods = ['PUT'])
def update_program(pid):
    if pid not in programs :
        return jsonify({"error": "program not found"}), 404
    data = request.json
    programs[pid].updat(data)
    return jsonify(programs[pid]),200

if _name_ == '__main__':
    app.run(debug=True)


